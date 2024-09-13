import pyautogui
import time

# Function to simulate key press with a duration
def press_key(key, duration=0.1):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

# Example: Move forward and tell unit to follow
press_key('w')  # Move hero forward
press_key('c')  # Command unit to follow
press_key('a')  # Move Hero left
press_key('d')  # Move Hero right
# Example: Move backward and tell unit to attack
press_key('s')  # Move hero backward
press_key('v')  # Command unit to attack
