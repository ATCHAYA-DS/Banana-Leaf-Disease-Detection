# 🍌 Robust Banana Leaf Disease Detection

A beginner-friendly, AI-powered agricultural web application designed to help farmers, agronomists, and agricultural students diagnose banana leaf diseases early, accurately, and with full transparency.

---

## 🌟 Key Features

1. **Single Leaf & Whole Banana Plant Analysis**
   - Upload a close-up photo of an individual leaf.
   - Or upload a photo of an **entire banana plant**: the computer vision system automatically segments individual leaves, inspecting each leaf separately so farmers don't need to photograph each leaf individually.

2. **OpenCV Image Preprocessing Pipeline**
   - **Bilateral Filtering**: Eliminates camera sensor noise and digital artifacts while strictly preserving sharp leaf veins and lesion borders.
   - **CLAHE (Contrast Limited Adaptive Histogram Equalization)**: Balances harsh outdoor sunlight glare and dark leaf shadows in the LAB color space.

3. **CNN Disease Detection (4 Target Classes)**
   - 🌿 **Healthy Banana Leaf**
   - 🍂 **Black Sigatoka** (*Pseudocercospora fijiensis*)
   - 🍂 **Yellow Sigatoka** (*Pseudocercospora musae*)
   - 🍂 **Panama Disease / Fusarium Wilt** (*Fusarium oxysporum*)

4. **Explainable AI (Grad-CAM Visual Heatmaps)**
   - Generates visual attention heatmaps (JET colormap) overlaid on the leaf image.
   - Highlights the exact symptomatic necrotic lesions or chlorotic streaks that triggered the diagnostic decision, eliminating the "black-box" dilemma.

5. **Multi-Language Support (6 Languages)**
   - 🌐 **English**
   - 🌐 **Tamil (தமிழ்)**
   - 🌐 **Hindi (हिन्दी)**
   - 🌐 **Telugu (తెలుగు)**
   - 🌐 **Malayalam (മലയാളം)**
   - 🌐 **Kannada (ಕನ್ನಡ)**
   - Instant language switching across all navigation, buttons, disease names, diagnoses, explanations, recommendations, and dashboard metrics.

6. **Farmer Voice Assistant (Text-to-Speech)**
   - Read aloud button with audio playback in the farmer's selected language using the Web Speech Synthesis API.

7. **Practical Farmer Recommendations & Prevention**
   - Actionable cultural, sanitary, drainage, and biological practices.
   - Explicit safety disclaimer: no unsafe pesticide dosages; recommendations emphasize verification with local Krishi Vigyan Kendras (KVK) or extension officers.

8. **Farmer Surveillance Dashboard & SQLite Database**
   - Tracks total images analyzed, healthy vs. diseased counts, and visual disease distribution.
   - Searchable scan history with image thumbnails, timestamps, and deep-dive result views.

9. **Safe Demo Mode & Transparent Model Integration**
   - If a trained deep learning model is not yet placed in `/model`, the application automatically runs in **DEMO MODE** using computer vision heuristics, clearly labeled on the interface without misleading accuracy claims.

---

## 📁 Project Folder Structure

```
robust-banana-disease-detection/
│
├── app.py                      # Main Flask web application backend and routing
├── requirements.txt            # Python dependencies (Flask, OpenCV, NumPy, Pillow)
├── README.md                   # Comprehensive documentation and setup guide
├── test_app.py                 # Automated unit and integration test suite
├── create_sample_images.py     # Script to generate sample test images
├── train_model.py              # CNN training script (MobileNetV2 transfer learning)
│
├── database_manager.py         # SQLite database management for scan history
├── image_processing.py         # OpenCV preprocessing, segmentation, and Grad-CAM
├── model_handler.py            # CNN inference engine and transparent Demo Mode
├── translations.py             # Multi-language dictionary for 6 languages
│
├── templates/                  # Jinja2 HTML Templates
│   ├── base.html               # Shared layout, navbar, language selector, footer
│   ├── index.html              # Home page with upload form, mode toggle, features
│   ├── result.html             # Visual comparison, Grad-CAM, advice, voice player
│   ├── dashboard.html          # Farmer statistics, distribution chart, history table
│   └── about.html              # Plant pathology details, technical pipeline guide
│
├── static/                     # Static Web Assets
│   ├── css/
│   │   └── style.css           # Clean green and white responsive agriculture stylesheet
│   ├── js/
│   │   └── script.js           # Drag-drop, preview, language switcher, voice player
│   └── images/                 # Sample test images for demonstration
│
├── model/                      # Machine Learning Model Directory
│   ├── README.md               # Instructions on how and where to place trained model
│   └── banana_disease_model.h5 # (Place your trained Keras/TensorFlow model here)
│
├── uploads/                    # Stores uploaded images, preprocessed files, and XAI maps
│   ├── xai/                    # Grad-CAM heatmap overlays
│   └── segments/               # Cropped leaf segments from whole plant images
│
└── database/                   # Database Directory
    └── app.db                  # SQLite database storing diagnosis history
```

---

## 🚀 Step-by-Step Instructions to Run Locally

### Step 1: Open Your Terminal or Command Prompt
Navigate to the project directory:
```bash
cd c:\Users\TOSHIBA\Desktop\viji
```

### Step 2: Verify Python Installation
Make sure Python 3.9+ is installed:
```bash
python --version
```

### Step 3: Install Required Dependencies
Run:
```bash
pip install -r requirements.txt
```
*Note: Flask, OpenCV, NumPy, and Pillow are installed. If you wish to train or run custom CNN neural networks locally, you can additionally install TensorFlow (`pip install tensorflow`). When TensorFlow is not installed, the application automatically runs in safe Demo Mode.*

### Step 4: Run the Web Application
Start the Flask development server:
```bash
python app.py
```

You will see output similar to:
```
=======================================================
 Robust Banana Leaf Disease Detection Server Starting 
 Mode: DEMO MODE (Heuristics)
 Local URL: http://127.0.0.1:5000
=======================================================
 * Running on http://127.0.0.1:5000
```

### Step 5: Open in Your Browser
Open your web browser (Google Chrome, Edge, Firefox, or Safari) and go to:
```
http://127.0.0.1:5000
```

---

## 🧪 Testing the Application

To run the automated test suite verifying database operations, OpenCV preprocessing, whole-plant segmentation, Grad-CAM generation, and all Flask endpoints:
```bash
python -m unittest test_app.py
```

Sample test images are already generated and available in `static/images/`:
- `sample_healthy_leaf.jpg`
- `sample_black_sigatoka.jpg`
- `sample_yellow_sigatoka.jpg`
- `sample_whole_plant.jpg`

You can upload any of these sample images directly on the homepage to test the workflow!

---

## 🧠 Connecting a Trained Deep Learning CNN Model

1. **Where to Place the Model:**
   Save your trained model file as:
   ```
   model/banana_disease_model.h5
   ```
2. **Class Order Requirement:**
   - Index 0: `Healthy`
   - Index 1: `Black Sigatoka`
   - Index 2: `Yellow Sigatoka`
   - Index 3: `Panama Disease`
3. **Training Script Included:**
   You can train a model using your dataset by running:
   ```bash
   python train_model.py --data_dir /path/to/dataset --epochs 15
   ```
4. **Automatic Detection:**
   When `banana_disease_model.h5` is placed in `model/` and TensorFlow is installed, the application automatically switches from **DEMO MODE** to **CNN MODEL ACTIVE** on restart.

---

## 🧑‍🌾 Agricultural Safety Disclaimer

This system is intended as an educational and advisory diagnostic aid for farmers and agricultural workers. **Do not apply chemical pesticides or untested chemical dosages based solely on automated predictions.** Always consult your local agricultural extension service, certified agronomist, or Krishi Vigyan Kendra (KVK) for officially approved regional management practices.
