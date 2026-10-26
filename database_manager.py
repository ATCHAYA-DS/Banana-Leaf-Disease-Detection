import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', 'app.db')

def get_connection():
    """Create and return a database connection with dict-like row access."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the SQLite database with the predictions table."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            filename TEXT NOT NULL,
            original_path TEXT NOT NULL,
            preprocessed_path TEXT,
            xai_path TEXT,
            analysis_mode TEXT DEFAULT 'single_leaf',
            disease_name TEXT NOT NULL,
            is_healthy INTEGER NOT NULL,
            confidence REAL NOT NULL,
            explanation TEXT,
            detected_leaves_count INTEGER DEFAULT 1,
            is_demo INTEGER DEFAULT 1
        )
    ''')
    conn.commit()
    conn.close()

def insert_prediction(filename, original_path, preprocessed_path, xai_path, 
                      analysis_mode, disease_name, is_healthy, confidence, 
                      explanation, detected_leaves_count=1, is_demo=1):
    """Insert a new prediction record into the database."""
    conn = get_connection()
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        INSERT INTO predictions (
            timestamp, filename, original_path, preprocessed_path, xai_path,
            analysis_mode, disease_name, is_healthy, confidence, 
            explanation, detected_leaves_count, is_demo
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        timestamp, filename, original_path, preprocessed_path, xai_path,
        analysis_mode, disease_name, int(is_healthy), float(confidence),
        explanation, detected_leaves_count, int(is_demo)
    ))
    
    record_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return record_id

def get_prediction_by_id(record_id):
    """Retrieve a single prediction by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM predictions WHERE id = ?', (record_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def get_recent_predictions(limit=10):
    """Get the most recent predictions."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM predictions ORDER BY id DESC LIMIT ?', (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_dashboard_stats():
    """Calculate aggregated stats for the farmer dashboard."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Total count
    cursor.execute('SELECT COUNT(*) AS total FROM predictions')
    total = cursor.fetchone()['total']
    
    # Healthy vs Diseased count
    cursor.execute('SELECT COUNT(*) AS healthy FROM predictions WHERE is_healthy = 1')
    healthy = cursor.fetchone()['healthy']
    
    diseased = total - healthy
    
    # Disease breakdown
    cursor.execute('''
        SELECT disease_name, COUNT(*) as count 
        FROM predictions 
        GROUP BY disease_name 
        ORDER BY count DESC
    ''')
    breakdown_rows = cursor.fetchall()
    breakdown = {row['disease_name']: row['count'] for row in breakdown_rows}
    
    # Recent history (last 15 records)
    cursor.execute('SELECT * FROM predictions ORDER BY id DESC LIMIT 15')
    recent = [dict(r) for r in cursor.fetchall()]
    
    conn.close()
    return {
        'total': total,
        'healthy': healthy,
        'diseased': diseased,
        'breakdown': breakdown,
        'recent': recent
    }

def clear_history():
    """Clear all records from predictions table."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM predictions')
    conn.commit()
    conn.close()
