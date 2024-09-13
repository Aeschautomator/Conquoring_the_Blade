from pynput import keyboard
import time

def on_press(key):
    try:
        print(f'{key.char} pressed at {time.time()}')
    except AttributeError:
        print(f'{key} pressed at {time.time()}')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
