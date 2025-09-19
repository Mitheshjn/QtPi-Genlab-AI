import cv2

# Load the image (✅ fixed path with parentheses and quotes)
image = cv2.imread(r"D:\myspace\annufeed\WhatsApp Image 2025-04-13 at 6.35.23 PM.jpeg")

if image is None:
    print("Error: Image not found or unable to open")
    exit()

# Get image dimensions
h, w, _ = image.shape

# Define center point
center_x, center_y = w // 2, h // 2

# Define a small square region around the center (10x10 pixels)
region_size = 10
x1, y1 = center_x - region_size, center_y - region_size
x2, y2 = center_x + region_size, center_y + region_size

# Crop that region
center_region = image[y1:y2, x1:x2]

# Calculate average color in the region
avg_color = center_region.mean(axis=0).mean(axis=0)  # (B, G, R)
b, g, r = avg_color

print(f"Center RGB Values: R={int(r)}, G={int(g)}, B={int(b)}")

# Show the image with rectangle around the center
output = image.copy()
cv2.rectangle(output, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.imshow("Center Region", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
