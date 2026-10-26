"""
Robust Banana Leaf Disease Detection
A Beginner-Friendly, Multi-Language, Farmer-Centric Web Application.
"""

import os
import uuid
from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory, flash
from werkzeug.utils import secure_filename

# Local helper modules
from database_manager import init_db, insert_prediction, get_prediction_by_id, get_dashboard_stats, clear_history
from image_processing import preprocess_image, segment_whole_plant, generate_gradcam_overlay
from model_handler import predict_disease, get_model, IS_DEMO_MODE, CLASSES
from translations import TRANSLATIONS

app = Flask(__name__)
app.secret_key = "robust-banana-leaf-ai-secret-key"

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
XAI_FOLDER = os.path.join(UPLOAD_FOLDER, 'xai')
SEGMENTS_FOLDER = os.path.join(UPLOAD_FOLDER, 'segments')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload limit

# Ensure required upload directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(XAI_FOLDER, exist_ok=True)
os.makedirs(SEGMENTS_FOLDER, exist_ok=True)

# Initialize database table on startup
init_db()

def allowed_file(filename):
    """Check if the uploaded file has a supported image extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_current_lang():
    """Retrieve selected language from cookie, query param, or default to English."""
    lang = request.args.get('lang') or request.cookies.get('app_lang') or 'en'
    if lang not in TRANSLATIONS:
        lang = 'en'
    return lang

@app.context_processor
def inject_context():
    """Inject language dictionary and demo status into all Jinja2 templates."""
    lang = get_current_lang()
    return {
        'current_lang': lang,
        't': TRANSLATIONS.get(lang, TRANSLATIONS['en']),
        'all_translations': TRANSLATIONS,
        'is_demo_mode': IS_DEMO_MODE,
        'classes': CLASSES
    }

@app.route('/')
def index():
    """Home page with image upload interface, feature showcase, and instructions."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle image upload, preprocessing, whole-plant segmentation (if selected),
    CNN inference or demo mode prediction, and Grad-CAM XAI generation."""
    if 'image' not in request.files:
        flash("No image file provided. Please choose a photo.", "warning")
        return redirect(url_for('index'))

    file = request.files['image']
    if file.filename == '':
        flash("No file selected. Please choose a banana leaf or plant photo.", "warning")
        return redirect(url_for('index'))

    if not allowed_file(file.filename):
        flash("Invalid image format! Only JPG, JPEG, and PNG are supported.", "danger")
        return redirect(url_for('index'))

    analysis_mode = request.form.get('mode', 'single_leaf')
    lang = request.form.get('lang', get_current_lang())
    if lang not in TRANSLATIONS:
        lang = 'en'

    # Save original uploaded image with unique identifier
    orig_filename = secure_filename(file.filename)
    unique_id = uuid.uuid4().hex[:10]
    ext = orig_filename.rsplit('.', 1)[1].lower()
    saved_filename = f"{unique_id}_{orig_filename}"
    original_path = os.path.join(app.config['UPLOAD_FOLDER'], saved_filename)
    file.save(original_path)

    # Preprocessing with OpenCV (Noise reduction & CLAHE lighting balance)
    prep_filename = f"prep_{unique_id}.jpg"
    preprocessed_path = os.path.join(app.config['UPLOAD_FOLDER'], prep_filename)
    
    try:
        bgr_prep, tensor = preprocess_image(original_path, preprocessed_path)
    except Exception as e:
        flash(f"Image preprocessing failed: {str(e)}", "danger")
        return redirect(url_for('index'))

    model = get_model()

    if analysis_mode == 'whole_plant':
        # Whole-plant analysis: segment individual leaves
        try:
            overview_abs_path, leaf_crops = segment_whole_plant(original_path, SEGMENTS_FOLDER)
            overview_rel_path = os.path.relpath(overview_abs_path, BASE_DIR).replace('\\', '/')
            
            leaf_results = []
            diseased_found = False
            top_severity_disease = "Healthy"
            highest_conf = 0.0

            for leaf in leaf_crops:
                # Preprocess cropped leaf segment
                l_prep_name = f"prep_{leaf['filename']}"
                l_prep_path = os.path.join(SEGMENTS_FOLDER, l_prep_name)
                l_bgr_prep, l_tensor = preprocess_image(leaf['filepath'], l_prep_path)
                
                # Predict disease on this leaf
                pred = predict_disease(l_tensor, l_bgr_prep)
                
                # Generate Grad-CAM for this leaf
                xai_leaf_name = f"xai_{leaf['filename']}"
                xai_leaf_path = os.path.join(XAI_FOLDER, xai_leaf_name)
                generate_gradcam_overlay(
                    l_bgr_prep, 
                    model=model, 
                    preprocessed_tensor=l_tensor,
                    predicted_class_name=pred['disease_name'],
                    output_path=xai_leaf_path
                )
                
                if not pred['is_healthy']:
                    diseased_found = True
                    if pred['confidence'] > highest_conf:
                        top_severity_disease = pred['disease_name']
                        highest_conf = pred['confidence']

                leaf_results.append({
                    "leaf_number": leaf['leaf_number'],
                    "crop_url": url_for('uploaded_file', filename=f"segments/{leaf['filename']}"),
                    "xai_url": url_for('uploaded_file', filename=f"xai/{xai_leaf_name}"),
                    "disease_name": pred['disease_name'],
                    "is_healthy": pred['is_healthy'],
                    "confidence": pred['confidence'],
                    "area_pct": leaf['area_percentage']
                })

            overall_disease = top_severity_disease if diseased_found else "Healthy"
            overall_healthy = not diseased_found
            overall_confidence = highest_conf if diseased_found else 92.5
            
            # Overview XAI overlay on whole plant
            xai_filename = f"xai_{unique_id}.jpg"
            xai_path = os.path.join(XAI_FOLDER, xai_filename)
            generate_gradcam_overlay(
                bgr_prep, 
                model=model, 
                preprocessed_tensor=tensor,
                predicted_class_name=overall_disease,
                output_path=xai_path
            )

        except Exception as e:
            flash(f"Whole plant segmentation encountered an error: {str(e)}", "danger")
            return redirect(url_for('index'))
    else:
        # Single Leaf Analysis
        overview_rel_path = None
        leaf_results = []
        
        pred = predict_disease(tensor, bgr_prep)
        overall_disease = pred['disease_name']
        overall_healthy = pred['is_healthy']
        overall_confidence = pred['confidence']

        # Generate Grad-CAM Heatmap overlay
        xai_filename = f"xai_{unique_id}.jpg"
        xai_path = os.path.join(XAI_FOLDER, xai_filename)
        generate_gradcam_overlay(
            bgr_prep, 
            model=model, 
            preprocessed_tensor=tensor,
            predicted_class_name=overall_disease,
            output_path=xai_path
        )

    # Retrieve disease info and localized explanation
    lang_dict = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    disease_details = lang_dict['disease_info'].get(overall_disease, lang_dict['disease_info']['Healthy'])
    explanation_text = disease_details['explanation']

    # Log into SQLite database
    record_id = insert_prediction(
        filename=orig_filename,
        original_path=f"uploads/{saved_filename}",
        preprocessed_path=f"uploads/{prep_filename}",
        xai_path=f"uploads/xai/{xai_filename}",
        analysis_mode=analysis_mode,
        disease_name=overall_disease,
        is_healthy=1 if overall_healthy else 0,
        confidence=overall_confidence,
        explanation=explanation_text,
        detected_leaves_count=len(leaf_results) if analysis_mode == 'whole_plant' else 1,
        is_demo=1 if IS_DEMO_MODE else 0
    )

    return render_template(
        'result.html',
        record_id=record_id,
        analysis_mode=analysis_mode,
        original_image=url_for('uploaded_file', filename=saved_filename),
        preprocessed_image=url_for('uploaded_file', filename=prep_filename),
        xai_image=url_for('uploaded_file', filename=f"xai/{xai_filename}"),
        overview_image=url_for('uploaded_file', filename=os.path.basename(overview_rel_path)) if overview_rel_path else None,
        leaf_results=leaf_results,
        disease_name=overall_disease,
        localized_disease_name=disease_details['name'],
        is_healthy=overall_healthy,
        confidence=overall_confidence,
        explanation=explanation_text,
        recommendations=disease_details['recommendations'],
        prevention_tips=disease_details['prevention'],
        is_demo=IS_DEMO_MODE,
        selected_lang=lang
    )

@app.route('/result/<int:record_id>')
def view_result(record_id):
    """View details of a past prediction from database history."""
    record = get_prediction_by_id(record_id)
    if not record:
        flash("Diagnosis record not found.", "warning")
        return redirect(url_for('dashboard'))

    lang = get_current_lang()
    lang_dict = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    disease_details = lang_dict['disease_info'].get(record['disease_name'], lang_dict['disease_info']['Healthy'])

    return render_template(
        'result.html',
        record_id=record['id'],
        analysis_mode=record['analysis_mode'],
        original_image=url_for('static_or_upload', path=record['original_path']),
        preprocessed_image=url_for('static_or_upload', path=record['preprocessed_path']),
        xai_image=url_for('static_or_upload', path=record['xai_path']),
        overview_image=None,
        leaf_results=[],
        disease_name=record['disease_name'],
        localized_disease_name=disease_details['name'],
        is_healthy=bool(record['is_healthy']),
        confidence=record['confidence'],
        explanation=disease_details['explanation'],
        recommendations=disease_details['recommendations'],
        prevention_tips=disease_details['prevention'],
        is_demo=bool(record['is_demo']),
        selected_lang=lang
    )

@app.route('/dashboard')
def dashboard():
    """Farmer surveillance dashboard showing totals, health ratios, and scan history."""
    stats = get_dashboard_stats()
    return render_template('dashboard.html', stats=stats)

@app.route('/about')
def about():
    """About project page detailing disease symptoms, agronomic practices, and AI training."""
    return render_template('about.html')

@app.route('/api/clear_history', methods=['POST'])
def clear_db_history():
    """Clear all records from database history."""
    clear_history()
    flash("Diagnosis history has been cleared successfully.", "info")
    return redirect(url_for('dashboard'))

@app.route('/api/translations')
def get_translations_api():
    """API returning all language dictionaries for instant client-side switching."""
    return jsonify(TRANSLATIONS)

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    """Serve uploaded images securely."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/file/<path:path>')
def static_or_upload(path):
    """Helper route to serve saved path references."""
    if path.startswith('uploads/'):
        rel = path.replace('uploads/', '', 1)
        return send_from_directory(app.config['UPLOAD_FOLDER'], rel)
    return send_from_directory(BASE_DIR, path)

if __name__ == '__main__':
    print("\n=======================================================")
    print(" Robust Banana Leaf Disease Detection Server Starting ")
    print(f" Mode: {'DEMO MODE (Heuristics)' if IS_DEMO_MODE else 'TRAINED CNN ACTIVE'}")
    print(" Local URL: http://127.0.0.1:5000")
    print("=======================================================\n")
    app.run(debug=True, host='127.0.0.1', port=5000)
