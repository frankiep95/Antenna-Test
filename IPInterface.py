import paramiko


class IPInterface():
    def __init__(self, ip_address, username="root", password="rWaveTech"):
        self.__ip_address = ip_address
        self.__username = username
        self.__password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    
    def setIP(self, ip_address):
        self.__ip_address = ip_address

    def connect(self):
        try:
            self.client.connect(
                hostname=self.__ip_address,
                username=self.__username,
                password=self.__password,
                look_for_keys=False,
                allow_agent=False
            )
            return True
        except Exception as e:
            print(f"Failed to connect to {self.__ip_address}: {e}")
            return False
        except paramiko.AuthenticationException:
            print(f"Authentication failed for {self.__ip_address}. Please verify your credentials.")
            return False
        except Exception as e:
            print(f"An error occurred while connecting to {self.__ip_address}: {e}")
            return False    

    def disconnect(self):
        self.client.close()
        self.connected = False  

    def command(self, cmd):
        try:
           stdin, stdout, stderr = self.client.exec_command(cmd)
           return stdout.read().decode()
        except Exception as e:
            print(f"Failed to execute command '{cmd}' on {self.__ip_address}: {e}")

    
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

