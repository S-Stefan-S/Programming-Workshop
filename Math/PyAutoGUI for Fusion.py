import pyautogui
from time import sleep

screenWidth, screenHeight = pyautogui.size()
pyautogui.PAUSE = 0.6

length = []
with open('/Users/qiyshen/Coding/Programming-Workshop/Math/Cosine wave data.txt') as inputfile:
    for line in inputfile:
        length.append(line.strip().split(','))

def repeat():
    element_number = 150
    x = 370
    y = 600
    row = 11
    pyautogui.hotkey('Ctrl', 'left')
    #420,120, 50 in x
    for i in range(5):
        x = 370
        for i in range(15):
            pyautogui.moveTo(x, y,)
            pyautogui.click()
            pyautogui.typewrite('e')
            pyautogui.typewrite(str(length[element_number]))
            pyautogui.PAUSE = 0.2
            pyautogui.press('left')
            pyautogui.press('delete')
            pyautogui.press('left')
            pyautogui.press('delete')
            pyautogui.press('left')
            pyautogui.press('left')
            pyautogui.press('left')
            pyautogui.press('left')
            pyautogui.press('left')
            pyautogui.press('delete')
            pyautogui.press('left')
            pyautogui.press('delete')
            pyautogui.PAUSE = 0.6
            pyautogui.moveTo(332, 433,)
            pyautogui.click()
            pyautogui.typewrite('r')
            pyautogui.moveTo(1391, 310,)
            pyautogui.click()
            pyautogui.moveTo(1391, 310,)
            pyautogui.click()
            pyautogui.press('esc')
            pyautogui.hotkey('command', 'v')
            pyautogui.moveTo(111, 232,)
            pyautogui.click()
            x += 50
            element_number += 1
        if row != 1:
            y += 50
        else:
            y += 30
        row += 1
        pyautogui.hotkey('Ctrl', 'right')
        pyautogui.hotkey('Ctrl', 'left')

repeat()
