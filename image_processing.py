"""
OpenCV Image Preprocessing, Whole-Plant Leaf Segmentation,
and Explainable AI (Grad-CAM / Lesion Saliency Heatmap) Engine.
"""

import cv2
import numpy as np
import os
import uuid

def preprocess_image(input_path, output_path=None, target_size=(224, 224)):
    """
    OpenCV Preprocessing Pipeline:
    1. Reads image from input_path.
    2. Bilateral Filter for edge-preserving noise reduction.
    3. CLAHE (Contrast Limited Adaptive Histogram Equalization) on LAB Lightness channel
       to normalize sunlight glare, shadow imbalances, and outdoor lighting conditions.
    4. Saves the enhanced image to output_path if provided.
    5. Returns (bgr_processed, rgb_normalized_tensor_for_model).
    """
    img = cv2.imread(input_path)
    if img is None:
        raise ValueError(f"Could not read image from {input_path}")

    # 1. Bilateral filtering: smooths noise while keeping leaf veins and spot edges sharp
    filtered = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

    # 2. Lighting & Shadow Correction via CLAHE on LAB Color Space
    lab = cv2.cvtColor(filtered, cv2.COLOR_BGR2LAB)
    l_channel, a_channel, b_channel = cv2.split(lab)
    
    # ClipLimit=2.5 prevents over-amplification of noise in flat leaf surfaces
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    l_equalized = clahe.apply(l_channel)
    
    lab_equalized = cv2.merge((l_equalized, a_channel, b_channel))
    bgr_preprocessed = cv2.cvtColor(lab_equalized, cv2.COLOR_LAB2BGR)

    # Save preprocessed version if path specified
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        cv2.imwrite(output_path, bgr_preprocessed)

    # Prepare normalized array for model input (224x224x3, RGB, values in [0, 1])
    resized_rgb = cv2.cvtColor(bgr_preprocessed, cv2.COLOR_BGR2RGB)
    resized_rgb = cv2.resize(resized_rgb, target_size, interpolation=cv2.INTER_AREA)
    normalized_tensor = resized_rgb.astype(np.float32) / 255.0
    normalized_tensor = np.expand_dims(normalized_tensor, axis=0) # shape (1, 224, 224, 3)

    return bgr_preprocessed, normalized_tensor

def segment_whole_plant(input_path, output_dir, max_leaves=4):
    """
    Analyzes a whole banana plant image:
    1. Segments leaf foliage regions from background and soil using HSV color thresholds.
    2. Identifies prominent individual leaf contours.
    3. Crops individual leaves and saves them into output_dir.
    4. Draws green diagnostic bounding boxes on the full plant overview image.
    5. Returns (overview_image_path, list_of_leaf_data_dicts).
    """
    img = cv2.imread(input_path)
    if img is None:
        raise ValueError(f"Could not read image from {input_path}")

    h, w = img.shape[:2]
    total_area = h * w
    os.makedirs(output_dir, exist_ok=True)

    # Convert to HSV to separate foliage from sky, soil, and trunks
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Mask for healthy green leaves
    lower_green = np.array([25, 30, 30])
    upper_green = np.array([90, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Mask for yellowing / necrotic / chlorotic foliage
    lower_yellow = np.array([12, 30, 30])
    upper_yellow = np.array([25, 255, 255])
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Mask for dark necrotic spots/streaks
    lower_dark = np.array([0, 30, 15])
    upper_dark = np.array([30, 255, 120])
    mask_dark = cv2.inRange(hsv, lower_dark, upper_dark)

    foliage_mask = cv2.bitwise_or(mask_green, mask_yellow)
    foliage_mask = cv2.bitwise_or(foliage_mask, mask_dark)

    # Morphological operations to group leaf segments and remove small background noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
    cleaned_mask = cv2.morphologyEx(foliage_mask, cv2.MORPH_CLOSE, kernel)
    cleaned_mask = cv2.morphologyEx(cleaned_mask, cv2.MORPH_OPEN, kernel)

    # Find contours representing individual leaves or prominent clusters
    contours, _ = cv2.findContours(cleaned_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter by minimum area (at least 1.5% of total image area)
    min_leaf_area = total_area * 0.015
    valid_contours = [c for c in contours if cv2.contourArea(c) > min_leaf_area]
    
    # Sort by area descending and take top N
    valid_contours = sorted(valid_contours, key=cv2.contourArea, reverse=True)[:max_leaves]

    annotated_overview = img.copy()
    detected_leaves = []

    # If no large contours were found (e.g. image was already cropped leaf), treat whole image as one
    if not valid_contours:
        leaf_id = uuid.uuid4().hex[:8]
        crop_filename = f"leaf_1_{leaf_id}.jpg"
        crop_path = os.path.join(output_dir, crop_filename)
        cv2.imwrite(crop_path, img)
        detected_leaves.append({
            "leaf_number": 1,
            "filename": crop_filename,
            "filepath": crop_path,
            "bbox": (0, 0, w, h),
            "area_percentage": 100.0
        })
    else:
        for idx, cnt in enumerate(valid_contours, start=1):
            x, y, box_w, box_h = cv2.boundingRect(cnt)
            
            # Add a slight padding around leaf for context
            pad_x = int(box_w * 0.05)
            pad_y = int(box_h * 0.05)
            x0 = max(0, x - pad_x)
            y0 = max(0, y - pad_y)
            x1 = min(w, x + box_w + pad_x)
            y1 = min(h, y + box_h + pad_y)

            leaf_crop = img[y0:y1, x0:x1]
            leaf_id = uuid.uuid4().hex[:8]
            crop_filename = f"leaf_{idx}_{leaf_id}.jpg"
            crop_path = os.path.join(output_dir, crop_filename)
            cv2.imwrite(crop_path, leaf_crop)

            # Draw prominent emerald bounding box and tag on overview image
            cv2.rectangle(annotated_overview, (x0, y0), (x1, y1), (46, 125, 50), 3)
            label = f"Leaf #{idx}"
            cv2.putText(annotated_overview, label, (x0 + 8, y0 + 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 4, cv2.LINE_AA)
            cv2.putText(annotated_overview, label, (x0 + 8, y0 + 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (46, 125, 50), 2, cv2.LINE_AA)

            detected_leaves.append({
                "leaf_number": idx,
                "filename": crop_filename,
                "filepath": crop_path,
                "bbox": (x0, y0, x1 - x0, y1 - y0),
                "area_percentage": round((cv2.contourArea(cnt) / total_area) * 100, 1)
            })

    # Save overview image with annotations
    overview_id = uuid.uuid4().hex[:8]
    overview_filename = f"overview_{overview_id}.jpg"
    overview_path = os.path.join(output_dir, overview_filename)
    cv2.imwrite(overview_path, annotated_overview)

    return overview_path, detected_leaves

def generate_gradcam_overlay(image_bgr, model=None, preprocessed_tensor=None, 
                             predicted_class_name="Healthy", output_path=None):
    """
    Explainable AI (XAI) Grad-CAM Generator:
    - If a trained TensorFlow model is active, calculates true class activation map
      using gradients of the predicted class score w.r.t the last convolutional layer.
    - If in DEMO MODE (no model weights), calculates symptom saliency map based on
      leaf tissue anomalies (chlorosis, necrotic lesions, leaf streak margins).
    - Overlays heatmap using OpenCV JET colormap onto the original leaf image.
    - Saves and returns the output path.
    """
    h, w = image_bgr.shape[:2]
    heatmap_matrix = None

    # Check if a genuine Keras model was passed and TensorFlow is functioning
    if model is not None and preprocessed_tensor is not None:
        try:
            import tensorflow as tf
            # Find the last 4D convolutional layer in the model
            conv_layers = [layer.name for layer in model.layers if 'conv' in layer.name.lower()]
            if conv_layers:
                last_conv_name = conv_layers[-1]
                grad_model = tf.keras.models.Model(
                    inputs=[model.inputs],
                    outputs=[model.get_layer(last_conv_name).output, model.output]
                )
                with tf.GradientTape() as tape:
                    conv_outputs, predictions = grad_model(preprocessed_tensor)
                    class_idx = tf.argmax(predictions[0])
                    loss = predictions[:, class_idx]

                grads = tape.gradient(loss, conv_outputs)
                pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

                conv_outputs = conv_outputs[0]
                heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
                heatmap = tf.squeeze(heatmap)
                heatmap = tf.maximum(heatmap, 0) / (tf.math.reduce_max(heatmap) + 1e-10)
                heatmap_matrix = heatmap.numpy()
        except Exception as e:
            # Fall back to computer vision saliency if TF Grad-CAM encounters an exception
            heatmap_matrix = None

    # Computer Vision Symptomatic Saliency (for Demo Mode or robust fallback)
    if heatmap_matrix is None:
        # Convert to HSV & LAB
        hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
        lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2LAB)
        
        # Calculate color variance from healthy green leaf baseline (H ~ 55, S ~ 160, V ~ 120)
        h_ch, s_ch, v_ch = cv2.split(hsv)
        l_ch, a_ch, b_ch = cv2.split(lab)

        if predicted_class_name == "Healthy":
            # For healthy leaf: attention is evenly distributed along healthy veins and lamina
            healthy_mask = cv2.inRange(hsv, np.array([30, 40, 40]), np.array([85, 255, 255]))
            attention = cv2.GaussianBlur(healthy_mask.astype(np.float32), (31, 31), 0)
        elif predicted_class_name == "Black Sigatoka":
            # Necrotic streaks: dark brown/black elongated spots with low V and moderate H
            streak_mask = cv2.inRange(hsv, np.array([5, 40, 10]), np.array([28, 255, 100]))
            edge_spots = cv2.Canny(image_bgr, 50, 150)
            combined = cv2.bitwise_or(streak_mask, edge_spots)
            attention = cv2.GaussianBlur(combined.astype(np.float32), (25, 25), 0)
        elif predicted_class_name == "Yellow Sigatoka":
            # Yellow chlorotic rings and gray center spots
            yellow_mask = cv2.inRange(hsv, np.array([18, 50, 80]), np.array([36, 255, 255]))
            gray_center = cv2.inRange(lab, np.array([100, 115, 115]), np.array([180, 140, 140]))
            combined = cv2.bitwise_or(yellow_mask, gray_center)
            attention = cv2.GaussianBlur(combined.astype(np.float32), (29, 29), 0)
        else: # Panama Disease
            # Outer margin yellowing and vascular wilt discoloration
            wilt_mask = cv2.inRange(hsv, np.array([15, 40, 60]), np.array([32, 255, 255]))
            attention = cv2.GaussianBlur(wilt_mask.astype(np.float32), (35, 35), 0)

        # Normalize attention map to [0, 1]
        norm_max = np.max(attention)
        if norm_max > 0:
            heatmap_matrix = attention / norm_max
        else:
            heatmap_matrix = np.zeros((h, w), dtype=np.float32)

    # Resize heatmap to match original image dimensions
    heatmap_resized = cv2.resize(heatmap_matrix, (w, h))
    heatmap_uint8 = np.uint8(255 * heatmap_resized)

    # Apply JET Colormap (Blue = Low importance, Yellow/Red = High disease activation)
    heatmap_color = cv2.applyColorMap(heatmap_uint8, cv2.COLORMAP_JET)

    # Superimpose heatmap with original image (40% heatmap + 60% original image)
    gradcam_blended = cv2.addWeighted(image_bgr, 0.62, heatmap_color, 0.38, 0)

    # Save XAI image if output path provided
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        cv2.imwrite(output_path, gradcam_blended)

    return gradcam_blended
