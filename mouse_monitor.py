from pynput import mouse
class MouseMonitor:
    def on_move(x,y):
        print(f'pointer moved (x={x}, y={y})')
        pass
    def on_click(x,y,button,pressed):
        if not pressed:
            return False
    def on_scroll():
        pass