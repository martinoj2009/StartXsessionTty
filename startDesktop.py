#!/usr/bin/python

# This will prompt for the desktop type and launch the desktop of your choice in the TTY

from os import ttyname, listdir, system
from sys import stdout, stdin
from re import search
from io import open
from subprocess import getstatusoutput

# Make sure requirements are meet
# Have sx installed
if getstatusoutput('sx')[0] != 0:
    print('Error! You need to have sx installed. Please install sx package to start x session')
    exit(-11)


# Get the TTY name
TTY = str(ttyname(stdout.fileno())).split('/')[2].replace('tty','')

# Get the desktop environments installed on this system
DESKTOPS = listdir('/usr/share/xsessions')

# Present the list of desktops available to the user
print('Enter the number for the desktop you wish to use:\n')

INDEX = 0
for desktop in DESKTOPS:
    print('[' + str(INDEX) + ']' + ' ' +str(desktop).replace('.desktop',''))
    INDEX = INDEX+1

# Get the desktop selected by the user
ENTEREDINDEX = False
SEARCH = None
SELECTEDINDEX = None
EXEC = None

while SELECTEDINDEX == None:
    USERENTERED = input()

    # Check input
    SEARCH = search("\d", USERENTERED)
    if SEARCH:
        SELECTEDINDEX = int(SEARCH.group(0))
    else:
        print("Please enter a valid number")

print('\nSelected: ' + DESKTOPS[SELECTEDINDEX])

# Now get the command needed to start the desktop session
FILE = open('/usr/share/xsessions/' + DESKTOPS[SELECTEDINDEX], "rb")
for line in FILE:
    try:
        if line.decode('utf8').startswith("Exec="):
            EXEC = ' '.join(line.decode('utf8').split('=')[1:]).rstrip()
    except:
        # Ignore the line
        continue

# Start the desktop session
system('sx ' + EXEC + " -- :1 vt" + TTY)
