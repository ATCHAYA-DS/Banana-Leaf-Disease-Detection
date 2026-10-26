"""
Automated End-to-End Test Suite for Robust Banana Leaf Disease Detection
Verifies:
1. SQLite Database operations
2. OpenCV Preprocessing (CLAHE, Bilateral filtering)
3. Whole-Plant Leaf Segmentation
4. Grad-CAM XAI Heatmap generation
5. Multi-Language Translations dictionary completeness
6. Flask web routes and prediction workflow
"""

import os
import sys
import unittest
import cv2
import numpy as np
import io

from app import app
import database_manager
from image_processing import preprocess_image, segment_whole_plant, generate_gradcam_overlay
from model_handler import predict_disease, IS_DEMO_MODE, CLASSES
from translations import TRANSLATIONS

class BananaDiseaseDetectionTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        cls.client = app.test_client()
        cls.sample_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'images')
        cls.healthy_sample = os.path.join(cls.sample_dir, 'sample_healthy_leaf.jpg')
        cls.plant_sample = os.path.join(cls.sample_dir, 'sample_whole_plant.jpg')

    def test_database_initialization_and_operations(self):
        """Test database table creation, insertion, and retrieval."""
        database_manager.init_db()
        rec_id = database_manager.insert_prediction(
            filename="unit_test_leaf.jpg",
            original_path="uploads/test.jpg",
            preprocessed_path="uploads/prep_test.jpg",
            xai_path="uploads/xai/xai_test.jpg",
            analysis_mode="single_leaf",
            disease_name="Healthy",
            is_healthy=1,
            confidence=94.5,
            explanation="Test healthy leaf explanation",
            detected_leaves_count=1,
            is_demo=1
        )
        self.assertIsNotNone(rec_id)
        
        record = database_manager.get_prediction_by_id(rec_id)
        self.assertIsNotNone(record)
        self.assertEqual(record['disease_name'], "Healthy")
        self.assertEqual(record['is_healthy'], 1)
        self.assertAlmostEqual(record['confidence'], 94.5)

        stats = database_manager.get_dashboard_stats()
        self.assertGreaterEqual(stats['total'], 1)
        self.assertIn('Healthy', stats['breakdown'])

    def test_image_preprocessing(self):
        """Test bilateral filtering and CLAHE shadow/lighting correction."""
        self.assertTrue(os.path.exists(self.healthy_sample), "Sample healthy leaf must exist")
        out_prep = os.path.join(os.path.dirname(self.healthy_sample), 'temp_prep_test.jpg')
        
        bgr_prep, tensor = preprocess_image(self.healthy_sample, out_prep)
        self.assertIsNotNone(bgr_prep)
        self.assertEqual(tensor.shape, (1, 224, 224, 3))
        self.assertTrue(os.path.exists(out_prep))
        if os.path.exists(out_prep):
            os.remove(out_prep)

    def test_whole_plant_segmentation(self):
        """Test leaf isolation from whole banana plant photo."""
        self.assertTrue(os.path.exists(self.plant_sample), "Sample whole plant must exist")
        seg_dir = os.path.join(os.path.dirname(self.plant_sample), 'temp_segments')
        
        overview_path, leaves = segment_whole_plant(self.plant_sample, seg_dir, max_leaves=4)
        self.assertTrue(os.path.exists(overview_path))
        self.assertGreaterEqual(len(leaves), 1)
        for leaf in leaves:
            self.assertTrue(os.path.exists(leaf['filepath']))
            # Cleanup temp leaf files
            if os.path.exists(leaf['filepath']):
                os.remove(leaf['filepath'])
        if os.path.exists(overview_path):
            os.remove(overview_path)
        if os.path.exists(seg_dir):
            os.rmdir(seg_dir)

    def test_gradcam_generation(self):
        """Test Explainable AI Grad-CAM heatmap generation."""
        img = cv2.imread(self.healthy_sample)
        out_xai = os.path.join(os.path.dirname(self.healthy_sample), 'temp_xai_test.jpg')
        
        xai_img = generate_gradcam_overlay(
            img, 
            model=None, 
            preprocessed_tensor=None,
            predicted_class_name="Healthy",
            output_path=out_xai
        )
        self.assertIsNotNone(xai_img)
        self.assertEqual(xai_img.shape, img.shape)
        self.assertTrue(os.path.exists(out_xai))
        if os.path.exists(out_xai):
            os.remove(out_xai)

    def test_translations_completeness(self):
        """Test that all 6 required languages are defined and have disease info."""
        required_langs = ['en', 'ta', 'hi', 'te', 'ml', 'kn']
        for lang in required_langs:
            self.assertIn(lang, TRANSLATIONS, f"Language {lang} missing from TRANSLATIONS")
            t = TRANSLATIONS[lang]
            self.assertIn('app_title', t)
            self.assertIn('btn_analyze', t)
            self.assertIn('disease_info', t)
            for cls in CLASSES:
                self.assertIn(cls, t['disease_info'], f"Class {cls} missing in {lang}")

    def test_web_routes(self):
        """Test Flask GET routes for home, dashboard, about, translations API."""
        r_home = self.client.get('/')
        self.assertEqual(r_home.status_code, 200)
        self.assertIn(b"Robust Banana Leaf Disease Detection", r_home.data)

        r_dash = self.client.get('/dashboard')
        self.assertEqual(r_dash.status_code, 200)

        r_about = self.client.get('/about')
        self.assertEqual(r_about.status_code, 200)

        r_trans = self.client.get('/api/translations')
        self.assertEqual(r_trans.status_code, 200)
        self.assertTrue(r_trans.is_json)

    def test_predict_endpoint_single_leaf(self):
        """Test end-to-end image upload and prediction workflow."""
        with open(self.healthy_sample, 'rb') as f:
            data = {
                'image': (io.BytesIO(f.read()), 'test_leaf.jpg'),
                'mode': 'single_leaf',
                'lang': 'en'
            }
            response = self.client.post('/predict', data=data, content_type='multipart/form-data')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Disease Diagnosis Results", response.data)
            self.assertIn(b"Grad-CAM", response.data)

if __name__ == '__main__':
    unittest.main()
