from __future__ import print_function
import math

z = 0
a = []


def series(i):
    x = z
    x = 0
    for n in range(i):
        x += 0 + (5 * n)
        # x += 0 + (10 * n)
        # x += 250 - (4.5 * n)
    print(x)


def sequence(i):
    b = a
    b = []
    for n in range(i):
        c = 10*(((math.cos((1+2.3*n)/3))*3)+6)
        b.append(c)
    one_decimals = ["%.1f" % c for c in b]
    print(*one_decimals, sep = '\n')


# choose sequence or serie

# diplay choices

def display_choices():
    print("\n\n[1]sequence")
    print("[2]series")


def decision(choice):
    if choice == 1:
        sequence(input("Enter the term number: "))
    elif choice == 2:
        series(input("Enter the term number: "))
    else:
        print("Error!")


while True:
    display_choices()
    decision(input("Enter a choice: "))
