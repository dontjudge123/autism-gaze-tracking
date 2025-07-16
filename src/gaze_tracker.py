import cv2

def start_gaze_tracking():
    print("[INFO] Gaze tracking started (simulated)...")
    cap = cv2.VideoCapture(0) 

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w = frame.shape[:2]
        cv2.circle(frame, (w//2, h//2), 10, (0, 255, 0), -1)

        cv2.imshow("Gaze Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Gaze tracking stopped.")
