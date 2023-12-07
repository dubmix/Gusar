import logging

GREEN = '\033[92m'
RESET_PRINT = '\033[0m'

class ColoredText(logging.StreamHandler):
    def emit(self, record):
        msg = self.format(record)
        if record.levelno == logging.INFO:
            msg = f"{GREEN}{msg}{RESET_PRINT}"
        print(msg)

logging.basicConfig(
    format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[ColoredText()]
)
logger = logging.getLogger(__name__)