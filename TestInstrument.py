import IPInterface as ipi
from mainWindow import IP

class TestInstrument:
    def __init__(self, serialNumber):
        self.serialNumber = serialNumber
        self.interface = None
        self.folder = None
        self.connected = False
    
    def connect(self, ip_address):
        self.interface = ipi.IPInterface()
        self.interface.setIP(ip_address)
        if self.interface.connect():
            connectButton.config(text="Connected", bg="green")
            self.interface = unit

        else:
            connectButton.config(text="Failed to Connect", bg="red")

    def select_folder():
        folder_path = filedialog.askdirectory(title ="Select Folder to Save Test Data")
        if folder_path:
            pathLabel.config(text=folder_path)
            self.folder = folder_path
        else:
            pathLabel.config(text="No folder selected")

    def is_connected(self):
        return self.connected