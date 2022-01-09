import socket

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
    sock.connect("/var/tmp/socktest/testsock.sock")
    while True:
        text = input()
        if text == "exit":
            break
        sock.send(text.encode())
