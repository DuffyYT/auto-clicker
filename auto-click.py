#Importing the mouse module for simulating mouse button-clicks
import mouse
#importing time module for providing intervals b\w clicks
import time
#importing keyboard module to start autoclicker remotely
import keyboard

global counter
global key
global cps
global ti

def start():
    global counter
    counter = 1
    while counter == 1:
        if ti == 1:
            print("auto-clicker has started\n")
            for _ in range(int(cps)):
                mouse.click('left')
                time.sleep(1/int(cps))
            counter = 0
            print("process has been completed")
        if ti == 0:
            print("auto-clicker has started ::\n")
            for _ in range(int(cps)):
                mouse.click('left')
            counter = 0
            print("process has been completed ::")

key = str(input("Please provide a key. (It should be only 1 character):  "))

if key == '':
    key = 'r'
    print("Hotkey defaulted to r as nothing was provided by the user")
elif key != '':
    key = key
    print(f"Hotkey set to {key}")

try:
    cps = str(input("Please provide a cps:  "))
except:
    pass

if cps == '':
    cps = 5
    print("CPS defaulted to 5(five) as nothing was provide")
elif cps != '':
    cps = cps
    print(f"CPS set to {cps}")

ti = int(input("Do you want time interval between your clicks? (1/0):  "))
if ti == 1:
    print("set to True")
    ti = True
if ti == 0:
    print("set to False")
    ti = False
    
keyboard.on_press_key(key,lambda _:start())

temp = input("ENJOY!!")
