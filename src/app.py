import logging
import threading
import time

LOGGER = logging.getLogger(__name__)


def _main():
    exit_flag = threading.Event()
    thread_count = 5

    def worker(exit_flag):
        while exit_flag.is_set() is False:
            LOGGER.info("thread alive")
            exit_flag.wait(5)
        LOGGER.info("exit_flag set")

    for _ in range(thread_count):
        t = threading.Thread(target=worker, args=(exit_flag,))
        t.start()

    try:
        while True:
            exit_flag.wait(60 * 60 * 24)
    except KeyboardInterrupt:
        exit_flag.set()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    _main()
