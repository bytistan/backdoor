import time 

def upload(conn, cmd):
    file_name = cmd[1]
    
    with open(file_name, "rb") as f:
        while True:
            bytes_read = f.read(1024)

            if not bytes_read:
                break

            conn.sendall(bytes_read)


    conn.sendall(b"<END>")
    time.sleep(1)

def download(conn, cmd):
    file_name = cmd[1]
    
    with open(file_name, "wb") as f:
        while True:
            data = conn.recv(1024)

            if b"<END>" in data:
                f.write(data.replace(b"<END>",b""))
                break

            f.write(data)
