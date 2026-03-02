import tkinter as tk
from tkinter import Menu, ttk
from tkinter import filedialog
import styling
import IPInterface as ipi
import commands as k
import gpsTest as gps
import instrument as inst   

mainWindow = tk.Tk()
mainWindow.title("Antenna Test Harness")
mainWindow.geometry("800x600")
mainWindow.configure(bg="gray")

menu_bar = tk.Menu(mainWindow)
mainWindow.config(menu=menu_bar)  

add_instrument = Menu(menu_bar, tearoff=0)
add_instrument.add_command(label="Add Instrument")
add_instrument.add_command(label="Remove Instrument")
menu_bar.add_cascade(label="Instruments", menu=add_instrument)



conectedInstruments = []


#connect instrument
tk.Label(mainWindow, text="Enter IP Address:", font=("Arial", 12), bg="gray").pack(pady=10)
IP = tk.Entry(mainWindow, font=("Arial", 12), width=30)
IP.pack(pady=2)  

connectButton = tk.Button(mainWindow,text = "Connect", font=("Arial",12), command=lambda: inst.connect(IP.get()))
connectButton.pack(pady=20)

# Select a save location for test data
folderPickerButton = tk.Button(mainWindow, text="Select Folder to Save Test Data", font=("Arial", 12), command=lambda: inst.select_folder())
folderPickerButton.pack(pady=20) 
pathLabel = tk.Label(mainWindow, text="No folder selected", font=("Arial", 10), bg="gray")
pathLabel.pack(pady=10)


#test GPS button
GPSSetupButton = tk.Button(mainWindow, text="Setup GPS Antenna", font=("Arial", 12), command=lambda: gps.setupGPS(unit))
GPSSetupButton.pack(pady=20)    


#test wifi connection
testWiFiButton = tk.Button(mainWindow, text="Test WiFi Connection", font=("Arial", 12),command=lambda: k.getWiFiConnections(unit))
testWiFiButton.pack(pady=20)   


mainWindow.mainloop()