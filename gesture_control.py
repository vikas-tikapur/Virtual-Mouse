import pyautogui
import numpy as np
import time

class GestureControl:
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()
        self.last_click_time = 0
        self.last_screenshot_time = 0

    def convert_to_screen_coords(self, landmarks, frame_width, frame_height):
        x = int(landmarks.x * frame_width)
        y = int(landmarks.y * frame_height)
        screen_x = np.interp(x, [0, frame_width], [0, self.screen_width])
        screen_y = np.interp(y, [0, frame_height], [0, self.screen_height])
        return screen_x, screen_y

    def perform_action(self, hand_landmarks, frame_width, frame_height):
        index_tip = hand_landmarks.landmark[8]
        thumb_tip = hand_landmarks.landmark[4]
        middle_tip = hand_landmarks.landmark[12]

        index_x, index_y = self.convert_to_screen_coords(index_tip, frame_width, frame_height)
        thumb_x, thumb_y = self.convert_to_screen_coords(thumb_tip, frame_width, frame_height)
        middle_x, middle_y = self.convert_to_screen_coords(middle_tip, frame_width, frame_height)

        # Move mouse to index finger tip
        pyautogui.moveTo(index_x, index_y)

        # Click detection (index and thumb close)
        click_distance = np.hypot(thumb_x - index_x, thumb_y - index_y)
        if click_distance < 40:
            if time.time() - self.last_click_time > 0.5:
                pyautogui.click()
                self.last_click_time = time.time()

        # Screenshot detection (middle and thumb close)
        screenshot_distance = np.hypot(thumb_x - middle_x, thumb_y - middle_y)
        if screenshot_distance < 40:
            if time.time() - self.last_screenshot_time > 1:
                pyautogui.screenshot('screenshot.png')
                print("Screenshot taken!")
                self.last_screenshot_time = time.time()
