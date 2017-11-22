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
        # c = 0 + (5 * n)
        # c = 0 + (10 * n)
        c = 250 - (4.5 * n)
        b.append(c)
    print(b)


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
