"""
Helper script to generate sample test images for Banana Leaf Disease Detection:
1. Healthy Banana Leaf
2. Black Sigatoka Infected Leaf
3. Yellow Sigatoka Infected Leaf
4. Whole Banana Plant with Multiple Leaves
"""

import cv2
import numpy as np
import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'images')
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_healthy_leaf():
    img = np.ones((500, 500, 3), dtype=np.uint8) * 245
    # Base green leaf shape
    center = (250, 250)
    axes = (140, 220)
    cv2.ellipse(img, center, axes, -15, 0, 360, (45, 145, 55), -1)
    
    # Midrib (central vein)
    cv2.line(img, (200, 460), (290, 50), (60, 180, 80), 6)
    
    # Lateral parallel veins
    for y in range(80, 440, 28):
        offset = int((y - 250) * 0.2)
        cv2.line(img, (245 + offset, y), (140, y + 40), (50, 160, 65), 2)
        cv2.line(img, (245 + offset, y), (370, y - 10), (50, 160, 65), 2)

    # Add slight natural gradient
    noise = np.random.normal(0, 8, img.shape).astype(np.int16)
    noisy_img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    
    out_path = os.path.join(OUTPUT_DIR, 'sample_healthy_leaf.jpg')
    cv2.imwrite(out_path, noisy_img)
    print(f"Generated: {out_path}")

def generate_black_sigatoka_leaf():
    img = np.ones((500, 500, 3), dtype=np.uint8) * 245
    center = (250, 250)
    axes = (140, 220)
    # Yellowish-green compromised base
    cv2.ellipse(img, center, axes, -15, 0, 360, (40, 130, 70), -1)
    
    # Midrib
    cv2.line(img, (200, 460), (290, 50), (55, 160, 85), 6)
    
    # Lateral veins
    for y in range(80, 440, 28):
        offset = int((y - 250) * 0.2)
        cv2.line(img, (245 + offset, y), (140, y + 40), (45, 140, 75), 2)
        cv2.line(img, (245 + offset, y), (370, y - 10), (45, 140, 75), 2)

    # Black Sigatoka: dark reddish-black narrow streaks parallel to veins
    streaks = [
        ((170, 180), (220, 195)),
        ((180, 230), (240, 250)),
        ((280, 160), (340, 145)),
        ((270, 220), (350, 205)),
        ((190, 310), (240, 325)),
        ((270, 290), (330, 280)),
        ((160, 260), (210, 275)),
        ((290, 330), (340, 320)),
    ]
    for p1, p2 in streaks:
        # Dark necrotic center
        cv2.line(img, p1, p2, (20, 25, 35), 7)
        # Brownish halo
        cv2.line(img, p1, p2, (30, 50, 110), 3)

    noise = np.random.normal(0, 10, img.shape).astype(np.int16)
    noisy_img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    
    out_path = os.path.join(OUTPUT_DIR, 'sample_black_sigatoka.jpg')
    cv2.imwrite(out_path, noisy_img)
    print(f"Generated: {out_path}")

def generate_yellow_sigatoka_leaf():
    img = np.ones((500, 500, 3), dtype=np.uint8) * 245
    center = (250, 250)
    axes = (140, 220)
    # Pale green background
    cv2.ellipse(img, center, axes, -15, 0, 360, (50, 150, 100), -1)
    cv2.line(img, (200, 460), (290, 50), (60, 170, 110), 6)
    
    # Yellow Sigatoka: yellow elliptical spots with grey centers
    spots = [
        (190, 170), (210, 240), (180, 320),
        (300, 160), (320, 230), (300, 300),
        (260, 370), (230, 120)
    ]
    for cx, cy in spots:
        # Bright yellow halo
        cv2.ellipse(img, (cx, cy), (28, 14), -20, 0, 360, (30, 220, 240), -1)
        # Gray necrotic center
        cv2.ellipse(img, (cx, cy), (16, 7), -20, 0, 360, (110, 115, 120), -1)

    noise = np.random.normal(0, 10, img.shape).astype(np.int16)
    noisy_img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    
    out_path = os.path.join(OUTPUT_DIR, 'sample_yellow_sigatoka.jpg')
    cv2.imwrite(out_path, noisy_img)
    print(f"Generated: {out_path}")

def generate_whole_banana_plant():
    # 600x600 canvas representing whole tree
    img = np.ones((600, 600, 3), dtype=np.uint8) * 230
    
    # Ground/soil
    cv2.rectangle(img, (0, 500), (600, 600), (70, 110, 140), -1)
    
    # Pseudostem trunk
    cv2.fillPoly(img, [np.array([[275, 520], [325, 520], [315, 260], [285, 260]])], (50, 90, 110))
    
    # Leaf 1 (Top Left)
    cv2.ellipse(img, (200, 180), (120, 50), 30, 0, 360, (40, 140, 55), -1)
    cv2.line(img, (290, 250), (130, 140), (50, 160, 70), 4)

    # Leaf 2 (Top Right)
    cv2.ellipse(img, (400, 170), (130, 55), -25, 0, 360, (45, 145, 60), -1)
    cv2.line(img, (310, 250), (480, 130), (55, 165, 75), 4)

    # Leaf 3 (Middle Left with some spots)
    cv2.ellipse(img, (180, 290), (125, 45), 15, 0, 360, (35, 130, 75), -1)
    cv2.ellipse(img, (170, 285), (20, 10), 10, 0, 360, (20, 30, 40), -1) # spot
    cv2.line(img, (285, 280), (100, 300), (45, 145, 60), 4)

    # Leaf 4 (Middle Right)
    cv2.ellipse(img, (420, 280), (120, 48), -15, 0, 360, (40, 135, 50), -1)
    cv2.line(img, (315, 280), (500, 280), (50, 155, 65), 4)

    # Leaf 5 (Emerging shoot)
    cv2.ellipse(img, (300, 140), (40, 100), 0, 0, 360, (60, 175, 80), -1)

    noise = np.random.normal(0, 8, img.shape).astype(np.int16)
    noisy_img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    
    out_path = os.path.join(OUTPUT_DIR, 'sample_whole_plant.jpg')
    cv2.imwrite(out_path, noisy_img)
    print(f"Generated: {out_path}")

if __name__ == '__main__':
    generate_healthy_leaf()
    generate_black_sigatoka_leaf()
    generate_yellow_sigatoka_leaf()
    generate_whole_banana_plant()
    print("All sample images generated successfully!")
