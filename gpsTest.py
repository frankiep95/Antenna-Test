import IPInterface as ipi
import commands as k 

def setupGPS(device):
    if device.connected:
        try:
            want = k.atCommand(device, "AT+WANT?")
            if "Current: 1" in want:
                print("GPS antenna is powered on")
            else:
                print("GPS antenna is powered off, powering on now")
                k.atCommand(device, "AT+WANT=1")
                want = k.atCommand(device, "AT+WANT?")
                if "Current: 1" in want:
                    print("GPS antenna is now powered on")
                else:
                    print("Failed to power on GPS antenna")

        #     #set password
            k.atCommand(device, "AT!ENTERCND=\"A710\"")
            
            dedicatedAnt = k.atCommand(device, "AT!CUSTOM?")
            if "GPSSEL" in dedicatedAnt:
                setAnt = k.atCommand(device, "AT!CUSTOM=GPSSEL,0")
                if "GPSSEL,0" in setAnt:
                    print("GPS antenna is set to use the dedicated antenna")
        except Exception as e:
            print(f"An error occurred while setting up the GPS antenna: {e}")

def gpsStatus(device):
    if device.connected:
        try:
            gpsStatus = k.atCommand(device, "AT!GPSSTATUS?")
            print(f"GPS Status: {gpsStatus}")
        except Exception as e:
            print(f"An error occurred while checking GPS status: {e}")
