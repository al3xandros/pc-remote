# pc-remote
A web based remote control for your pc. Move your mouse, click and write remotely from a browser. 

# Disclaimer:
**Please use the provided software with caution!!! It was not made with security**
**in mind, therefore I hereby state that I do not take responsibility for**
**possible for your action**

## System requirements
- Python >= 3.6
- Flask >= 1.1.2
- PyAutoGUI >= 0.9.52

Works on all platforms that have Python >= 3.6. Tested on Linux, Windows.

--------------------------------------------------------------------------

# Usage
## setup

### Windows

Install requirements

> pip install -r requirements.txt
 
or

> pip install flask pyautogui

For remote usage allow python to pass through the 
firewall

### Linux / Mac

Install requirements

> pip3 install -r requirements.txt

or

> pip3 install flask pyautogui

For remote usage allow a port (default: 5000) in your firewall to let
you access it remotely


## Run

to run navigate to the folder containing the "pc-remote.py", open a terminal window
and run:

> python3 pc-remote.py

to exit the program return to the terminal and hit "Ctrl/command + c"

## Connecting
From a browser go to your machine's ip address and port
usually: 192.168.1.x:[port-number] and using the buttons displayed you
can move the mouse and write text

