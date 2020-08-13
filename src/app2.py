import logging
import os
import signal
import threading
import time

LOGGER = logging.getLogger(__name__)


def create_signal_handlers(exit_flag):
    def signal_handler(sig, frame):
        LOGGER.info("Signal %s detected", sig)
        exit_flag.set()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)


def _main():
    exit_flag = threading.Event()
    create_signal_handlers(exit_flag)

    while exit_flag.is_set() is False:
        time.sleep(5)
        LOGGER.info("...")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    _main()
