import IPInterface as ipi


def getICCID(device):
    if device.connected:
        try:
            iccid = ipi.atCommand(device, "AT+ICCID?")
            print(f"ICCID: {iccid}")
            return iccid
        except Exception as e:
            print(f"An error occurred while retrieving ICCID: {e}")

def selectSIM(device, simSlot):
    if device.connected:
        try:
            if simSlot == 0:
                ipi.atCommand(device, "AT!UIMS=0")
                print("SIM slot 1 selected")
            elif simSlot == 1:
                ipi.atCommand(device, "AT!UIMS=1")
                print("SIM slot 2 selected")
            else:
                print("Invalid SIM slot. Please select either 0 or 1.")
        except Exception as e:
            print(f"An error occurred while selecting SIM slot: {e}")