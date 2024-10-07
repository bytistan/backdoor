import socket 
from file_transfer import *

class Server:
    def __init__(self):
        self.ip = "192.168.1.106"
        self.port = 5000

        self.connection = socket.socket()
        self.connection.bind((self.ip,self.port))
        
        self.exception_cmd = {
            "download":download,
            "upload":upload
        }

    def listen(self):
        self.connection.listen(2)
        
        print("[+] Server start to listening: " + self.ip + ":" + str(self.port))

        conn, address = self.connection.accept()

        print("[+] Connection from: " + str(address))

        while True:

            message = input("->")
            
            cmd = message.split(" ")

            if len(cmd) > 0 and cmd[0] in self.exception_cmd.keys():
                function = self.exception_cmd.get(cmd[0])
                cmd[0] = "download" if cmd[0] == "upload" else "upload" 

                space = " "
                message = space.join(cmd)
                
                conn.send(message.encode())
                
                function(conn,cmd) 

            else:
                conn.send(message.encode())
            
            data = conn.recv(1024).decode() 

            if not data:
                break

            print(str(data))

        
        conn.close()


if __name__ == "__main__":
    server = Server()
    server.listen()

