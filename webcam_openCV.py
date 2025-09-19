import cv2
import numpy as np

# Open webcam (0 is default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Average R, G, B values
    R_avg = np.mean(rgb_frame[:, :, 0])
    G_avg = np.mean(rgb_frame[:, :, 1])
    B_avg = np.mean(rgb_frame[:, :, 2])

    # Show frame (optional)
    cv2.imshow('Webcam', frame)
    
    # Print averages
    print(f"Average R: {R_avg:.2f}, G: {G_avg:.2f}, B: {B_avg:.2f}")

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
