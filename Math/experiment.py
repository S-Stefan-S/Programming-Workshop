import pyautogui
length = []
with open('/Users/qiyshen/Coding/Programming-Workshop/Math/Cosine wave data.txt') as inputfile:
    for line in inputfile:
        length.append(line.strip().split(','))

element_number = 0
word = "Hello"

print(length[element_number])
print(all(isinstance(n, list) for n in length))
pyautogui.typewrite(str(length[0]))

