
z = 0
a = []
def series(i):
    x = z
    x = 0
    for n in range(i):
        x += enter_formula()
    print("\n", x)


def sequence(i):
    b = a
    b = []
    for n in range(i):
        c = enter_formula()
        b.append(c)
    print("\n", b)


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

def enter_formula():
    formula = raw_input("\n*The term number must be n.\nEnter a formula: ")
    for i in formula:
        if i in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            int(i)
            

while True:
    display_choices()
    decision(input("Enter a choice: "))