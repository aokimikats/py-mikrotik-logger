import logging


class LogWriter:
    def __init__(self, filename, log_format):
        logging.basicConfig(filename=filename, filemode="w", format=log_format, level=logging.ERROR)
        self.logger = logging.getLogger(__name__)

    def get_logger(self):
        return self.logger
