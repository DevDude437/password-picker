# Password Picker
This is a simple application that will generate a random password for you to use. Currently, it is only available for use in the command line on a computer.
# How to use (Instructions for Arch Linux):
Download the file password_picker.py into your downloads folder. 
Make sure you have Python 3 installed. 
Open the Terminal, and to make the script executable run the following commands:
`nano ~/run_password_picker.sh`
Now add the following command:
`#!/bin/bash
cd ~/Downloads
python3 password_picker.py`
Save and exit by typing CTRL + X then Y and ENTER to save.
Now run:
`chmod +x ~/run_password_picker.sh`
Now whenever you want to run the script, open the Terminal and just type:
`~/run_password_picker.sh`
I hope these instructions help. I have only tested this on Arch Linux, so if you run into any issues, open an issue or shoot me an email! 
