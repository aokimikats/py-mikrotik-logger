import socket
import datetime
import sys
import os
from threading import Thread
import time


class UDPListener(Thread):

    def __init__(self):
        Thread.__init__(self)

        # <Network settings>
        self.timeout = 60
        self.host = "192.168.0.250"
        self.port = 514
        self.addr = (self.host, self.port)
        # </Network settings>

        # <Server binding>
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind(self.addr)
        self.daemon = True
        self.start()
        # </Server binding>

    def run(self):
        while True:
            try:
                # <Socket cycle>
                data = self.server.recvfrom(4096)
                received_data = data[0]
                sender_addr = data[1]
                # </Socket cycle>

                # <Data parser>
                helper.printer(received_data, sender_addr)
                helper.writer(received_data)
                # </Data parser>

            # <Exception handlers>
            except socket.timeout:
                print('Timeout. {0} seconds have passed'.format(self.timeout))
            # </Exception handlers>


class Servo:
    def __init__(self):
        # <Check if logs directory exists>
        self.logfile_path = "C:/Logs/"
        self.logfile_folder = os.path.exists("C:/Users/SysAdmin/Logs")
        if not self.logfile_folder:
            print("No folder found at" + self.logfile_path)
            time.sleep(5)
            sys.exit()
        # </Check if logs directory exists>
        self.logfile = "C:/Users/SysAdmin/Logs/mikrotik_log.txt"

    @staticmethod
    def printer(received_data, sender_addr):
        """Printing log strings to log"""
        print("Received data: ", received_data)
        print("Received from: ", sender_addr)

    def writer(self, received_data):
        """Writing log strings to file"""
        logfile = open(self.logfile_path, "a")
        logfile.write(f"{datetime.datetime.now().replace(microsecond=0)} {received_data}")
        logfile.close()


helper = Servo()
main = UDPListener()

while True:
    try:
        pass
    except KeyboardInterrupt:
        print("Exiting")
        sys.exit()
