import sys
from termcolor import colored
import os
import subprocess

print colored('hello', 'red'), colored('world', 'green')

Kill = ""
Grep_Ps = ""

Kill = raw_input("\n\n\nEnter the process name: ")


# Grep_Ps = ("ps -ef | grep -i " + Kill + " | grep -v Helper | grep -v grep | awk '{print $2}'")


Grep_Ps = subprocess.check_output("ps -ef | grep -i " + Kill + " | grep -v Helper | grep -v grep | awk '{print $2}'", shell = True)



print(Grep_Ps)
 
os.system("kill " + Grep_Ps)
