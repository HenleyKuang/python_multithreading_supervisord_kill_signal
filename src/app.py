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
    thread_count = 5

    def worker(exit_flag):
        while exit_flag.is_set() is False:
            LOGGER.info("thread alive: %s", exit_flag.is_set())
            exit_flag.wait(5)
        LOGGER.info("exit_flag set")

    for _ in range(thread_count):
        t = threading.Thread(target=worker, args=(exit_flag,))
        t.start()

    while exit_flag.is_set() is False:
        time.sleep(2)
        LOGGER.info("...")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    _main()
