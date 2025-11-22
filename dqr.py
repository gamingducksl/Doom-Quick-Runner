import os
import time
import colorama
from colorama import Fore, Style

#Reset colors
print(Style.RESET_ALL)

#Get current directory (for debugging)
#print(os.getcwd())

#Startup message
print("Welcome to the Doom quick-runner. Please set your parameters below.")

#Bold text
print(Style.BRIGHT)

#User-defined parameters
port = input(Fore.BLUE + 'Please enter source port (example: crispy-doom) ')
iwadpath = input('Please enter path to iwad ')
pwadpath = input('Please enter path to pwad (if applicable) ')
demopath = input('Please enter path to demo (if applicable) ' + Style.RESET_ALL)

#Reset colors
print(Style.RESET_ALL)

#Attempting to launch message
print("Attempting to launch Doom with the set parameters.")

#If no source port is defined
if not port:

    print(Fore.RED + "No source port specified, exiting.")
    time.sleep(2)
    exit()

#If no iwad is defined
if not iwadpath:

    print(Fore.YELLOW + "No iwad path specified, running default iwad.")
    #Reset colors
    print(Style.RESET_ALL)
    time.sleep(2)
    os.system(port)
    exit()

#Reset colors
print(Style.RESET_ALL)

#Launching Doom with set parameters

#Reset colors
print(Style.RESET_ALL)
if iwadpath and pwadpath and demopath:

    os.system(port + " " + "-iwad " + iwadpath + " " + "-file " + pwadpath + " " + "-playdemo " + demopath)
    #Reset colors
    print(Style.RESET_ALL)
    exit()

if iwadpath and pwadpath:

    os.system(port + " " + "-iwad " + iwadpath + " " + "-file " + pwadpath)
    #Reset colors
    print(Style.RESET_ALL)
    exit()

if iwadpath and demopath:

    os.system(port + " " + "-iwad " + iwadpath + " " + "-playdemo " + demopath)
    #Reset colors
    print(Style.RESET_ALL)
    exit()

if iwadpath:

    os.system(port + " " + "-iwad " + iwadpath)
    #Reset colors
    print(Style.RESET_ALL)
    exit()
