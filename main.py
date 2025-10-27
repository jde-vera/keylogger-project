from pynput import keyboard
from keyboard_monitor import KeyboardMonitor
import threading
def run_listener():
    with keyboard.Listener(on_press=KeyboardMonitor.on_press,on_release=KeyboardMonitor.on_release) as listener:
        listener.join()
# create the keyboard listener object
if __name__ == '__main__':
    thread1 = threading.Thread(target=run_listener)
    thread1.start()
