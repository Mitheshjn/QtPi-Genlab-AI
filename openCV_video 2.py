import cv2
import numpy as np

# Load video (local file)
video_path = r"C:\Users\Shiya\Downloads\water_video.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break   # end of video

    # Calculate average color (BGR format)
    avg_color = frame.mean(axis=0).mean(axis=0)
    b, g, r = avg_color

    # Print the values (you can also log them frame by frame)
    print(f"Frame Avg → R={int(r)}, G={int(g)}, B={int(b)}")

    # Show the video frame
    cv2.imshow("Video Frame", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release and close windows
cap.release()
cv2.destroyAllWindows()
