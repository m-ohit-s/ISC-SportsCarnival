import inspect
import logging


class CustomLogger:
    def __init__(self,
                 filename="isc.log",
                 level=logging.DEBUG,
                 filemode='a',
                 log_format='%(asctime)s - %(levelname)s - %(message)s'
                 ):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)

        if not self.logger.handlers:
            self.file_handler = logging.FileHandler(filename, filemode)
            self.file_handler.setLevel(level)
            formatter = logging.Formatter(log_format)
            self.file_handler.setFormatter(formatter)
            self.logger.addHandler(self.file_handler)

    def debug(self, message: str, file_path: str = None):
        if file_path is None:
            file_path = inspect.stack()[1].filename
        self.logger.debug(f"{message} - {file_path}")

    def error(self, message: str, file_path: str = None):
        if file_path is None:
            file_path = inspect.stack()[1].filename
        self.logger.error(f"{message} - {file_path}")

    def info(self, message: str, file_path: str = None):
        if file_path is None:
            file_path = inspect.stack()[1].filename
        self.logger.info(f"{message} - {file_path}")

    def critical(self, message: str, file_path: str = None):
        if file_path is None:
            file_path = inspect.stack()[1].filename
        self.logger.critical(f"{message} - {file_path}")

    def warning(self, message: str, file_path: str = None):
        if file_path is None:
            file_path = inspect.stack()[1].filename
        self.logger.warning(f"{message} - {file_path}")
