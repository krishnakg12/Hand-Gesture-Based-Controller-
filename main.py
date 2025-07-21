import cv2
import mediapipe as mp
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController, Button

# Initialize MediaPipe Hands, keyboard controller, and mouse controller
mp_hands = mp.solutions.hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
keyboard = KeyboardController()
mouse = MouseController()
cp = cv2.VideoCapture(0)

# Variables for hand gesture detection
x1, x2, y1, y2 = 0, 0, 0, 0

while True:
    success, image = cp.read()
    if not success:
        print("Failed to capture frame. Exiting.")
        break

    image_height, image_width, _ = image.shape
    image = cv2.flip(image, 1)
    rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output_hands = mp_hands.process(rgb_img)
    all_hands = output_hands.multi_hand_landmarks

    if all_hands:
        try:
            hand = all_hands[0]  # Focus on the first detected hand
            one_hand_landmark = hand.landmark

            # Detect coordinates for key landmarks
            for id, lm in enumerate(one_hand_landmark):
                x = int(lm.x * image_width)
                y = int(lm.y * image_height)

                if id == 12:  # Tip of middle finger
                    x1 = x
                    y1 = y
                if id == 0:  # Wrist
                    x2 = x
                    y2 = y

            # Distance between wrist and middle finger tip
            distX = x1 - x2
            distY = y1 - y2

            # W, A, S, D Controls
            if distY > -140 and distY != 0:  # Move Backward (S)
                keyboard.release('d')
                keyboard.release('a')
                keyboard.release('w')
                keyboard.press('s')
                print("S")
            if distY < -200 and distY != 0:  # Move Forward (W)
                keyboard.release('s')
                keyboard.release('d')
                keyboard.release('a')
                keyboard.press('w')
                print("W")
            if distX < -100 and distX != 0:  # Move Left (A)
                keyboard.release('s')
                keyboard.release('d')
                keyboard.press('w')
                keyboard.press('a')
                print("A")
            if distX > 55 and distX != 0:  # Move Right (D)
                keyboard.release('a')
                keyboard.release('s')
                keyboard.press('w')
                keyboard.press('d')
                print("D")

            # Jump (Space)
            if one_hand_landmark[8].y < one_hand_landmark[12].y - 0.1:  # Index finger above middle finger
                keyboard.press(Key.space)
                print("Jump")

            # Crouch (Ctrl)
            if one_hand_landmark[0].y > max(one_hand_landmark[8].y, one_hand_landmark[12].y,
                                            one_hand_landmark[16].y, one_hand_landmark[20].y):
                keyboard.press(Key.ctrl)
                print("Crouch")

            # Shoot (Mouse Left Click)
            thumb_tip = one_hand_landmark[4]
            index_tip = one_hand_landmark[8]
            if abs(thumb_tip.x - index_tip.x) < 0.05 and abs(thumb_tip.y - index_tip.y) < 0.05:
                mouse.press(Button.left)
                mouse.release(Button.left)
                print("Shoot")

            # Reload (R)
            if (one_hand_landmark[4].x < one_hand_landmark[3].x and  # Thumb crosses to the left
                all(one_hand_landmark[tip].y < one_hand_landmark[0].y for tip in [8, 12, 16, 20])):  # Fingers up
                keyboard.press('r')
                print("Reload")

            # Sprint (Shift)
            if one_hand_landmark[8].y < one_hand_landmark[6].y and one_hand_landmark[12].y > one_hand_landmark[8].y:
                keyboard.press(Key.shift)
                print("Sprint")

        except ValueError as ve:
            print(f"Value Error: {ve}")
    else:
        # Release all keys when no hands are detected
        print('None')
        keyboard.release('d')
        keyboard.release('a')
        keyboard.release('w')
        keyboard.release('s')
        keyboard.release(Key.ctrl)
        keyboard.release(Key.shift)
        keyboard.release(Key.space)
        keyboard.release('r')

    # Visualization for debugging
    if all_hands:
        for hand in all_hands:
            for lm in hand.landmark:
                cx, cy = int(lm.x * image_width), int(lm.y * image_height)
                cv2.circle(image, (cx, cy), 5, (0, 255, 0), -1)

    cv2.imshow("Hand Tracking", image)

    # Exit on 'q' key press
    q = cv2.waitKey(1)
    if q == ord("q"):
        break

cp.release()
cv2.destroyAllWindows()
