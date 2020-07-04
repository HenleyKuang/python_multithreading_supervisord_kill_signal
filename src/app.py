import logging
import threading
import time

LOGGER = logging.getLogger(__name__)


def _main():

    def worker(thread_id, exit_flag):
        while True:
            if exit_flag.is_set():
                LOGGER.info("[%s] exit_flag set", thread_id)
                break
            time.sleep(5)
            LOGGER.info("[%s] thread alive", thread_id)

    exit_flag = threading.Event()
    thread_count = 5
    thread_list = []
    for thread_id in range(thread_count):
        t = threading.Thread(target=worker, args=(thread_id, exit_flag))
        thread_list.append(t)
        t.start()
    try:
        time.sleep(30)
    except KeyboardInterrupt:
        exit_flag.set()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    _main()
