import webrepl
import getpass

#WebRepl default port number
PORT_NUMBER = 8266

class Client:
    '''
    This Class represents a WebReplClient
    only one instance allowed!
    '''
    no_of_instances = 0

    def __init__(self,  pswd, ip_addr='192.168.43.63', port=PORT_NUMBER) -> None:
        '''
        Client constructor
        '''
        if Client.no_of_instances >= 1: 
            return
        else: 
            try:
                self.data = {'host':str(ip_addr),'port':port,'password':str(pswd),'debug':False}
                self.repl = webrepl.Webrepl(**self.data)
                version = self.repl.get_ver()
                print("Connection successful!\nMicroPython version: %d.%d.%d" % version)
                Client.no_of_instances += 1
            except:
                raise
    
    def communicate(self, command):
        response = self.repl.sendcmd(command)
        x = len(command)
        return response.decode('ascii')[x:]



## Main
if __name__ == "__main__":

    pwd = getpass.getpass(prompt="Enter webrepl password: ") #password prompt

    ip_addr = input("Enter device ip address: " ) #ip address prompt

    client = Client(pwd, ip_addr, PORT_NUMBER)
    #print(Client.no_of_instances)

    usr_command = ''

    while True:
        usr_command = input(">>> ")
        if usr_command == '/exit': 
            break
        else:
            response = client.communicate(usr_command) 
            print(response)
