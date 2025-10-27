**definition:** a keylogger is a software that records keystrokes typed on a keyboard

**definition** a callback function is what the listener object calls when an event occurs

**Steps**
1. first I need to create the call back functions
    1. the on_press function receives a key function
    2. the function receives the key parameter (which could be special keys on a keyboard or regular characters)
    3. keyboard.Key is a class that represents special, non character keys
        - for eg keyboard.key.enter is a field of the keyboard.key class
    4. keyboard.KeyCode is a class that represents regular, character keys
        - to access the value you use key.char
2. then I need to create the listener object
    1. the keyboard.Listener is a class that monitors keyboard events 
        - it watches for key presses and key releases
    2. the join method waits for the listener to finish 
        - to stop it your callbacks must return False  