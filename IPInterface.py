import paramiko

# client = paramiko.SSHClient()

# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# try:
#     client.connect(
#         hostname="192.168.50.75",
#         username="root",
#         password="rWaveTech",
#         look_for_keys=False,
#         allow_agent=False

#     )

#      # Execute a command
#     stdin, stdout, stderr = client.exec_command("ls -l")
#     print(stdout.read().decode())

# except paramiko.AuthenticationException:
#     print("Authentication failed. Please verify your credentials.")
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     # Close the connection
#     client.close()   



class IPInterface():
    def __init__(self, ip_address, username, password):
        self.__ip_address = ip_address
        self.__username = username
        self.__password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            self.client.connect(
                hostname=self.__ip_address,
                username=self.__username,
                password=password,
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

    def command(self, cmd):
        try:
            self.client.exec_command(cmd)
        except Exception as e:
            print(f"Failed to execute command '{cmd}' on {self.__ip_address}: {e}")