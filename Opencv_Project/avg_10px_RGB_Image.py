import cv2
import numpy as np

# ✅ Change this path to your image file
image_path = r"C:\Users\sudis\OneDrive\Pictures\Saved Pictures\rupanzel.jpg"

# Load the image
image = cv2.imread(image_path)

# Check if image loaded successfully
if image is None:
    raise FileNotFoundError(f"Could not load image at {image_path}")

# Get image dimensions
h, w, _ = image.shape

# Define center coordinates
cx, cy = w // 2, h // 2
half_size = 5  # 10px area → half = 5

# Extract 10x10 region
roi = image[cy - half_size:cy + half_size, cx - half_size:cx + half_size]

# Calculate average color (BGR → RGB)
mean_color = cv2.mean(roi)[:3]  
mean_rgb = (int(mean_color[2]), int(mean_color[1]), int(mean_color[0]))

print("Average RGB of 10x10 center region:", mean_rgb)

# (Optional) show image with rectangle
output = image.copy()
cv2.rectangle(output, (cx - half_size, cy - half_size), (cx + half_size, cy + half_size), (0, 255, 0), 1)
cv2.imshow("Center Region", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
