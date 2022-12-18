
import socket
import time
import datetime

#IP = socket.gethostbyname(socket.gethostname())
IP = "192.168.1.44"
#IP = "192.168.54.126"
#PORT = 1234
PORT = 6638
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    tryingToConnect = True
    while tryingToConnect:
        try:
            client.connect(ADDR)
            tryingToConnect = False
        except:
            print("FAILED. Sleep briefly & try again")
            tryingToConnect = True
            time.sleep(5)
            continue

    while True:
        dateAsString = str(datetime.datetime.now()) + "\n"
        client.send(dateAsString.encode())
        print(dateAsString)
        time.sleep(0.0001)

if __name__ == "__main__":
    main()