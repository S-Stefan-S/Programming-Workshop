from random import randint

#Random Generator

Number_list = []

for number in range(randint(0, 666)):
    Number_list.append(randint(0, randint(0, 666)))

print(Number_list)

New = 0

New = Number_list[0]
for number in Number_list:
    if New < number:
        New = number
    else:
        pass

print(New)

New = 0
for number in Number_list:
    New += number

print(New)