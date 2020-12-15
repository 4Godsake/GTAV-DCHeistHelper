from pynput import keyboard
from pynput.keyboard import Key

from hack import start_hacking
from task_killer import killTask

def on_press(key):
    if key == ACTIVATION_KEY:
        start_hacking()
    if key == Key.f5:
        killTask()

ACTIVATION_KEY = keyboard.KeyCode(char='`')
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
