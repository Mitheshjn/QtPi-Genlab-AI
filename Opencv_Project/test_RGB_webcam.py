import cv2
import numpy as np

# ✅ Open webcam (0 = default camera, change if you have multiple)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("⚠️ Could not access the webcam")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Get frame dimensions
    h, w, _ = frame.shape

    # Define 10x10 px center region
    cx, cy = w // 2, h // 2
    half_size = 5
    roi = frame[cy - half_size:cy + half_size, cx - half_size:cx + half_size]

    # Compute average RGB (convert from BGR)
    mean_color = cv2.mean(roi)[:3]
    mean_rgb = (int(mean_color[2]), int(mean_color[1]), int(mean_color[0]))

    # Print in console
    print("Average RGB (center 10x10):", mean_rgb)

    # (Optional) draw rectangle & display on screen
    cv2.rectangle(frame, (cx - half_size, cy - half_size), (cx + half_size, cy + half_size), (0, 255, 0), 1)
    cv2.imshow("Webcam Center RGB", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
