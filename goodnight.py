# Python script to shutdown computer

import os

shutdown = input("Do you wish to shutdown your computer? (Yes / No): ")

if shutdown == "No":
    print("Exited")
    exit()
else:
    os.system("sudo shutdown -h now")