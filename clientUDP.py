import socket
import time
import threading

class ClientUDP:
    def __init__(self, ip, port, auto_reconnect=True):
        self.ip = ip
        self.port = port
        self.auto_reconnect = auto_reconnect
        self.connected = False
        self.socket = None
        self.connect()

    def is_connected(self):
        return self.connected

    def send_message(self, message):
        try:
            message = str('%s<EOM>' % message).encode('utf-8')
            self.socket.send(message)
        except ConnectionRefusedError:
            self.disconnect()
        except ConnectionResetError:
            self.disconnect()

    def disconnect(self):
        self.connected = False
        if self.socket:
            self.socket.close()
        if self.auto_reconnect:
            time.sleep(1)
            self.connect()

    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.connect((self.ip, self.port))
            self.connected = True
        except (ConnectionRefusedError, ConnectionResetError):
            self.disconnect()
