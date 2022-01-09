import socket

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
    sock.bind("/var/tmp/socktest/testsock.sock")
    sock.listen()
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024)
        if data == b"":
            break
        print(data.decode())