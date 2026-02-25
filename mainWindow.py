import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import styling
import IPInterface

mainWindow = tk.Tk()
mainWindow.title("Antenna Test Harness")
mainWindow.geometry("800x600")
mainWindow.configure(bg="gray")


# IP Address Input for unit connection

def connect():
    IPInterface.raw_socket_connection("192.168.50.75",22)

    # unit = IPInterface(IP.get())
    # unit.connect()

tk.Label(mainWindow, text="Enter IP Address:", font=("Arial", 12), bg="gray").pack(pady=10)
IP = tk.Entry(mainWindow, font=("Arial", 12), width=30)
IP.pack(pady=2)  

connectButton = tk.Button(mainWindow,text = "Connect", font=("Arial",12), command=connect)
connectButton.pack(pady=20)






# Select a save location for test data

def select_folder():
    folder_path = filedialog.askdirectory(title ="Select Folder to Save Test Data")
    if folder_path:
        pathLabel.config(text=folder_path)

folderPickerButton = tk.Button(mainWindow, text="Select Folder to Save Test Data", font=("Arial", 12), command=select_folder)
folderPickerButton.pack(pady=20) 

# if folderPickerButton.cget:
#     selectedPath = folderPickerButton.cget("text")
pathLabel = tk.Label(mainWindow, text="No folder selected", font=("Arial", 10), bg="gray")
pathLabel.pack(pady=10)






mainWindow.mainloop()