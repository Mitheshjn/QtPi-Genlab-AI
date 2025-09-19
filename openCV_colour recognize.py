import cv2
import numpy as np

# Define a set of basic colors with their HSV ranges
colors_hsv = {
    "Red": [(np.array([0, 120, 70]), np.array([10, 255, 255])),
            (np.array([170, 120, 70]), np.array([180, 255, 255]))],
    "Orange": [(np.array([10, 100, 100]), np.array([25, 255, 255]))],
    "Yellow": [(np.array([25, 100, 100]), np.array([35, 255, 255]))],
    "Green": [(np.array([35, 100, 100]), np.array([85, 255, 255]))],
    "Cyan": [(np.array([85, 100, 100]), np.array([95, 255, 255]))],
    "Blue": [(np.array([95, 100, 100]), np.array([125, 255, 255]))],
    "Purple": [(np.array([125, 100, 100]), np.array([150, 255, 255]))],
    "Pink": [(np.array([150, 100, 100]), np.array([170, 255, 255]))],
    "White": [(np.array([0, 0, 200]), np.array([180, 30, 255]))],
    "Gray": [(np.array([0, 0, 40]), np.array([180, 30, 200]))],
    "Black": [(np.array([0, 0, 0]), np.array([180, 255, 40]))],
    "Brown": [(np.array([10, 100, 20]), np.array([20, 255, 200]))],
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    detected_colors = []

    # Check each defined color
    for color_name, ranges in colors_hsv.items():
        mask = None
        for lower, upper in ranges:
            if mask is None:
                mask = cv2.inRange(hsv, lower, upper)
            else:
                mask = mask | cv2.inRange(hsv, lower, upper)

        if cv2.countNonZero(mask) > 5000:  # threshold to avoid noise
            detected_colors.append(color_name)

    # Show detected colors on screen
    if detected_colors:
        text = "Detected: " + ", ".join(detected_colors)
    else:
        text = "Detected: None"

    cv2.putText(frame, text, (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3)
    cv2.putText(frame, text, (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("Color Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
