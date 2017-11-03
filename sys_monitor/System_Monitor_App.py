from __future__ import print_function
import os
from time import sleep
import subprocess
import sys


#Display a Title Bar Function
def Title_Bar():
    print("\t\t\t\t\t\t\t\t\t\t  *********************************")
    print("\t\t\t\t\t\t\t\t\t\t  ********* SYSTEM MONITOR ********")
    print("\t\t\t\t\t\t\t\t\t\t  *********************************\n\n")


#Display Majer Options Function
def MO():
    print("[0]Exit")
    print("[1]View running processes")
    print("[2]View all the users who logged in")

      
#Display Sub1-Options Function
def S1O():
    print("[0]Go back")
    print("[1]View Recent running process")
    print("[2]View All running processes at the moment\n*No Refresh")
    print("[3]Kill a currently running process")
    print("\n*Enter 'q' to quit")


#Display Sub2-Options Function
def S2O():
    print("[0]Go back")
    print("[1]View all the users who logged in through graphic interface")
    print("[2]View all the users who logged in through terminal")
    print("\n*Enter 'q' to quit")


#-----------------------------------------------------------------------------
#Transition

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

code='*'

def transition():
    os.system('clear')
    for i in range(100):
        # print("*", end="")
        # subprocess.call(['echo', '-n', '*'], shell=True)
        # os.system('echo -n "-"')
        bash_command('echo -ne "'+code+'"')
        sleep(0.01)
    os.system('clear')
    Title_Bar()

#Error
def error():
    os.system('clear')
    print('Please chosse in the correct formate.')
    sleep(1)
    transition()




#-----------------------------------------------------------------------------


choice_M = 3

choice_S1 = 0
choice_S2 = 0
Kill = ""
Grep_Ps = ""

#Select Majer Option
def Select_Majer_Option():
    MO()
    choice_M = int(raw_input("\n\n\nEnter a choice: "))
    if choice_M == 0:
        transition()
        sleep(1)
        os.system('clear')
        sys.exit()
    elif choice_M == 1:
        transition()
        Select_Sub1_Option()
    elif choice_M == 2:
        transition()
        Select_Sub2_Option()
    else:
        error()
        Select_Majer_Option()

#Select Sub1-Option
def Select_Sub1_Option():
    S1O()
    choice_S1 = int(raw_input("\n\n\nEnter a choice: "))
    if choice_S1 == 0:
        transition()
        Select_Majer_Option()
    elif choice_S1 == 1:
        transition()
        os.system('top')
    elif choice_S1 == 2:
        transition()
        os.system('top | less')
    elif choice_S1 == 3:
        transition()
        Kill = raw_input("\n\n\nEnter the process name: ")
        Grep_Ps = subprocess.check_output("ps -ef | grep -i " + Kill + " | grep -v Helper | grep -v grep | awk '{print $2}'", shell = True)
        os.system("kill " + Grep_Ps)
        print(Kill + " has been eliminated.")
        sleep(1.3)
    else:
        error()
        Select_Sub1_Option()

#Select Sub2-Option
def Select_Sub2_Option():
    S2O()
    choice_S2 = int(raw_input("\n\n\nEnter a choice: "))
    if choice_S2 == 0:
        transition()
        Select_Majer_Option()
    elif choice_S2 == 1:
        transition()
        os.system('last | grep console | less')
    elif choice_S2 == 2:
        transition()
        os.system('last | grep ttys | less')
    else:
        error()
        Select_Sub2_Option()


#-----------------------------------------------------------------------------
#Process
while choice_M != 0:
    #Display a Title Bar
    transition()

    #Display/Select Majer Options
    Select_Majer_Option()



    
