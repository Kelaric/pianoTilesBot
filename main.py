import pyautogui
import time
import keyboard
from pynput.mouse import Controller, Button
mouse = Controller()

def click(x,y):
    mouse.move(x, y)
    mouse.press(Button.left)
    time.sleep(0.01)
    mouse.release(Button.left)
    mouse.move(-x, -y)
if __name__ == '__main__':
    while keyboard.is_pressed('q') == False:
        if pyautogui.pixel(644, 430)[0] == 0:
            click(644, 430)
        if pyautogui.pixel(713, 430)[0] == 0:
            click(713, 430)
        if pyautogui.pixel(805, 430)[0] == 0:
            click(805, 430)
        if pyautogui.pixel(900, 430)[0] == 0:
            click(900, 430)


