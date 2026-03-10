import IPInterface as ipi


def setupGPS(device):
    if device.connected:
        try:
            want = ipi.atCommand(device, "AT+WANT?")
            if "Current: 1" in want:
                print("GPS antenna is powered on")
            else:
                print("GPS antenna is powered off, powering on now")
                ipi.atCommand(device, "AT+WANT=1")
                want = ipi.atCommand(device, "AT+WANT?")
                if "Current: 1" in want:
                    print("GPS antenna is now powered on")
                else:
                    print("Failed to power on GPS antenna")

        #     #set password
            ipi.atCommand(device, "AT!ENTERCND=\"A710\"")
            
            dedicatedAnt = ipi.atCommand(device, "AT!CUSTOM?")
            if "GPSSEL" in dedicatedAnt:
                setAnt = ipi.atCommand(device, "AT!CUSTOM=GPSSEL,0")
                if "GPSSEL,0" in setAnt:
                    print("GPS antenna is set to use the dedicated antenna")
        except Exception as e:
            print(f"An error occurred while setting up the GPS antenna: {e}")

def gpsStatus(device):
    if device.connected:
        try:
            gpsStatus = ipi.atCommand(device, "AT!GPSSTATUS?")
            print(f"GPS Status: {gpsStatus}")
        except Exception as e:
            print(f"An error occurred while checking GPS status: {e}")
