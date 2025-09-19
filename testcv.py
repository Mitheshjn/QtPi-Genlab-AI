import cv2
import numpy as np
image = cv2.imread(r"D:\chiken logo.png")
if image is None:
    raise FileNotFoundError(f"Could not load image at {image}")

h, w, _ = image.shape
cx, cy = w // 2, h // 2
half_size = 5  
roi = image[cy - half_size:cy + half_size, cx - half_size:cx + half_size]

mean_color = cv2.mean(roi)[:3]  
mean_rgb = (int(mean_color[2]), int(mean_color[1]), int(mean_color[0]))

print("Average RGB of 10x10 center region:", mean_rgb)
output = image.copy()
cv2.rectangle(output, (cx - half_size, cy - half_size), (cx + half_size, cy + half_size), (0, 255, 0), 1)
cv2.imshow("Center Region", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
