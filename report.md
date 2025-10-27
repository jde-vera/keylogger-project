**definition:** a keylogger is a software that records keystrokes typed on a keyboard

**definition** a callback function is what the listener object calls when an event occurs

**Steps to monitor keyboard**
1. first I need to create the call back functions
    1. the function receives the key parameter (special or regular keys)
    2. keyboard.Key is a class that represents special keys
        - for eg keyboard.key.enter is a field of the keyboard.key class
    3. keyboard.KeyCode is a class that represents regular keys
        - to access the value you use key.char
2. then I need to create the listener object
    1. the keyboard.Listener is a class that monitors keyboard events 
        - it watches for key presses and key releases
    2. the join method waits for the listener to finish 
        - to stop it your callbacks must return False  

**Steps to monitor mouse**
1. first I need to create the call back functions
    1. on_move
        - the listener object calls this when the mouse moves
    2. on_click
        - the listener object calls this when the mouse is pressed
        - if the mouse is pressed return True, False if released
    3. on_scroll
        - the listener object calls this when the mouse scrolls
        - x, y are the coordinates of the mouse pointer 
        - dx, dy is the amount scrolled horizontally and vertically respectively
2. then I need to create the listener object
    1. the mouse.Listener is a class that monitors mouse events