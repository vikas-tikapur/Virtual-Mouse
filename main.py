import cv2
from hand_tracking import HandTracking
from gesture_control import GestureControl

hand_tracker = HandTracking()
gesture_control = GestureControl()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip the frame horizontally to match gesture direction

    frame_height, frame_width, _ = frame.shape
    results = hand_tracker.detect_hands(frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            gesture_control.perform_action(hand_landmarks, frame_width, frame_height)

    frame = hand_tracker.draw_landmarks(frame, results)
    cv2.imshow("Gesture Mouse", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
