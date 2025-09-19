import cv2

cap = cv2.VideoCapture(0)  # webcam (use video file path if needed)

if not cap.isOpened():
    print("Error: Cannot open camera or video file")
    exit()

frame_count = 0  # counter

while frame_count < 4:   # loop only 4 times
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot read frame")
        break

    h, w, _ = frame.shape
    center_x, center_y = w // 2, h // 2
    region_size = 10
    x1, y1 = center_x - region_size, center_y - region_size
    x2, y2 = center_x + region_size, center_y + region_size

    center_region = frame[y1:y2, x1:x2]
    avg_color = center_region.mean(axis=0).mean(axis=0)
    b, g, r = avg_color

    print(f"Frame {frame_count+1} - Center RGB Values: R={int(r)}, G={int(g)}, B={int(b)}")

    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow("Video Color Detection", frame)

    # Wait 500ms (0.5 sec) between frames so you can see clearly
    cv2.waitKey(500)

    frame_count += 1  # increase counter

cap.release()
cv2.destroyAllWindows()

