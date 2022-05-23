import socket
import sys
from threading import Thread
import config_init
import log_writer


class Receiver(Thread):
    def __init__(self):
        Thread.__init__(self)

        # <Network settings>
        self.address = (Config.host, Config.port)
        # </Network settings>

        # <Server binding>
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind(self.address)
        # </Server binding>

        self.daemon = True
        self.start()

    def run(self):
        while True:
            try:
                # <Socket cycle>
                data = self.server.recvfrom(4096)
                sender_address, data_received = data[1], data[0]
                # </Socket cycle>

                # <Data parser>
                logger.info(data_received, sender_address)
                # </Data parser>

            # <Exception handlers>
            except socket.timeout:
                logger.error('Timeout. {0} seconds have passed'.format(Config.timeout))
            # </Exception handlers>


Config = config_init.Config()

log_format = "%(levelname)s %(asctime)s - %(message)s"
logger = log_writer.LogWriter(Config.filename, log_format).get_logger()

if __name__ == '__main__':
    Receiver()
    while True:
        try:
            pass
        except KeyboardInterrupt:
            print("Exiting")
            sys.exit()
