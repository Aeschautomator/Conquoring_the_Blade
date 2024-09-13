# Function to log key presses to a file
def log_action(action, duration=None):
    with open('key_log.txt', 'a') as f:
        if duration:
            f.write(f"{action} for {duration} seconds at {time.time()}\n")
        else:
            f.write(f"{action} at {time.time()}\n")

# Example usage of the log function during bot behavior
def press_key_with_logging(key, duration=0.1):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)
    log_action(key, duration)
