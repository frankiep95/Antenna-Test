

def atCommand(device,atCommand):
    try:
        device.command("rm -f output.log")
        device.command("cat < /dev/ttyUSB2 > output.log &")
        device.command(f"echo -e \"{atCommand}\\r\\n\" > /dev/ttyUSB2")
        print(f"SENDING: echo -e \"{atCommand}\\r\\n\" > /dev/ttyUSB2")
        device.command(f"pkill cat")
        return device.command("cat output.log")
       
    except Exception as e:
        print(f"Failed to execute AT command '{atCommand}': {e}")

