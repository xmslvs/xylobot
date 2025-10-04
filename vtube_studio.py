import keyboard
import time

def trigger_expression(response):
    expression = response["emotion_state"] 
    keypress = {
        'happy': "h", 
        'sad': "s", 
        'scared': "s+c",
        'angry': "a", 
        'embarrassed': "e", 
        'playful': "p", 
        'confident': "c", 
        'loved': "l",
        'remove': "r"
    }
    keyboard.send(keypress['remove'], do_release=True)
    time.sleep(0.4)
    keyboard.send(keypress[expression], do_release=True)
    print(keypress[expression])

