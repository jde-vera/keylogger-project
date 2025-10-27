from pynput import keyboard, mouse
from keyboard_monitor import KeyboardMonitor
from mouse_monitor import MouseMonitor
import threading
def run_keyboard_listener():
    with keyboard.Listener(on_press=KeyboardMonitor.on_press,on_release=KeyboardMonitor.on_release) as listener:
        listener.join()
def run_mouse_listener():
    with mouse.Listener(on_move=MouseMonitor.on_move,on_click=MouseMonitor.on_click,on_scroll=MouseMonitor.on_scroll) as listener:
        listener.join()
if __name__ == '__main__':
    thread1 = threading.Thread(target=run_keyboard_listener)
    thread2 = threading.Thread(target=run_mouse_listener)
    thread1.start()
    thread2.start()
