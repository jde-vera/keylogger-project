from pynput import keyboard

class KeyboardMonitor:
    login_details = ""
    @staticmethod
    def on_press(key):
        try:
            print(f"regular key pressed: {key.char}")
        except AttributeError:
            print(f"special key pressed: {key}")
        KeyboardMonitor.login_details + str(key)
    @staticmethod
    def on_release(key):
        if key==keyboard.Key.enter:
            return False
