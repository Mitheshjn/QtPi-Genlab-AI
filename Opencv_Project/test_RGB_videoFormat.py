import cv2
import numpy as np

# ✅ Change this path to your video file
video_path = r"C:\Users\sudis\Videos\RGB_colour.mp4"

# Open the video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise FileNotFoundError(f"⚠️ Could not open video at {video_path}")

# Process frame by frame
while True:
    ret, frame = cap.read()
    if not ret:
        break  # video ended

    # Get frame dimensions
    h, w, _ = frame.shape

    # Define center region (10x10 px)
    cx, cy = w // 2, h // 2
    half_size = 5
    roi = frame[cy - half_size:cy + half_size, cx - half_size:cx + half_size]

    # Calculate average RGB (OpenCV is BGR by default)
    mean_color = cv2.mean(roi)[:3]
    mean_rgb = (int(mean_color[2]), int(mean_color[1]), int(mean_color[0]))

    print("Average RGB of center region:", mean_rgb)

    # (Optional) show video with rectangle
    cv2.rectangle(frame, (cx - half_size, cy - half_size), (cx + half_size, cy + half_size), (0, 255, 0), 1)
    cv2.imshow("Video Center RGB", frame)

    # Press 'q' to quit early
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
