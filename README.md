# StartXsessionTty
This script will allow you to start an Xsession inside a TTY. You can boot your computer into the terminal and only user the desktop when you need it. 

I made this script for my Arch Linux system as I didn't always need the desktop, but occasionally I would like to have a GUI.

# How it works
When you run this script it will get the current desktop environments you have installed on your system, then allow you to pick from a menu which desktop environment you would like to run. The desktop environment will then kick off under your login session and once you're done, you just logoff and drop back to the terminal.

# What's required?
You will need to have Python3 and sx installed. sx is for kicking off the xsession.
