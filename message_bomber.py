import pyautogui
import time
import sys

count = 0

try:
    while True:
        time.sleep(0.1)
        msg = 'hello'
        pyautogui.write(msg)
        pyautogui.press('enter')
        count += 1
        if count == 1:
            print('1 Message sent.')
        else:
            print(f'{count} Messages sent.')
        
except KeyboardInterrupt:
    print('\nScript ended :( by CTRL+C')
    print(f'{msg} was sent {count} times.')
    sys.exit(0)