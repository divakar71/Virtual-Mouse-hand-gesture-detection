import cv2
import mediapipe as mp
import pyautogui

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Get screen size
screen_width, screen_height = pyautogui.size()

# Variables to store locked hand tracking
locked_hand_wrist = None
hand_present = False

# Capture video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip and convert frame
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        if locked_hand_wrist is None:
            locked_hand_wrist = results.multi_hand_landmarks[0].landmark[0]
            hand_present = True

        detected_hands = results.multi_hand_landmarks
        hand_found = False

        for hand_landmarks in detected_hands:
            wrist = hand_landmarks.landmark[0]

            if abs(wrist.x - locked_hand_wrist.x) < 0.05 and abs(wrist.y - locked_hand_wrist.y) < 0.05:
                hand_found = True

                # Fingertips
                index_tip = hand_landmarks.landmark[8]
                middle_tip = hand_landmarks.landmark[12]
                ring_tip = hand_landmarks.landmark[16]
                pinky_tip = hand_landmarks.landmark[20]
                thumb_tip = hand_landmarks.landmark[4]
                thumb_ip = hand_landmarks.landmark[3]

                # MCP joints
                index_mcp = hand_landmarks.landmark[5]
                middle_mcp = hand_landmarks.landmark[9]
                ring_mcp = hand_landmarks.landmark[13]
                pinky_mcp = hand_landmarks.landmark[17]

                # Count non-thumb fingers
                fingers_up = [
                    index_tip.y < index_mcp.y,
                    middle_tip.y < middle_mcp.y,
                    ring_tip.y < ring_mcp.y,
                    pinky_tip.y < pinky_mcp.y
                ]

                # Improved thumb detection (based on x distance from joint)
                thumb_up = abs(thumb_tip.x - thumb_ip.x) > 0.04
                fingers_up.append(thumb_up)

                total_fingers = sum(fingers_up)

                # Convert index position for mouse
                x, y = int(index_tip.x * screen_width), int(index_tip.y * screen_height)

                # Gesture actions
                if total_fingers == 5:
                    pyautogui.scroll(-30)  # Scroll down
                elif total_fingers == 4:
                    pyautogui.scroll(30)   # Scroll up
                elif total_fingers == 3:
                    pyautogui.click(button='right')
                elif total_fingers == 2:
                    pyautogui.click(button='left')
                elif total_fingers == 1:
                    pyautogui.moveTo(x, y)

                # Draw landmarks
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        if not hand_found:
            locked_hand_wrist = None
            hand_present = False
    else:
        locked_hand_wrist = None
        hand_present = False

    # Show video
    cv2.imshow("Hand Gesture Mouse Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
