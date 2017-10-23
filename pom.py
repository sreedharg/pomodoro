import time
import os
import sys
import logging

logger = logging.getLogger('pomodoro')

class Pomodoro(object):
    def __init__(self, timeout):
        self._init_logger()
        self.timeout = timeout
        self.time_left = timeout

    def _init_logger(self):
        logger.setLevel(logging.INFO)

        logfile_name = 'pomodoro.log'

        fh = logging.FileHandler(logfile_name)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        fh.setLevel(logging.DEBUG)

        logger.addHandler(fh)
        logger.info("start: " + sys.argv[1])

    def _display_status(self):
        os.system('cls')
        print('\n\n\n         [', end='')
        print((25 - self.time_left) * '*' , end='' )
        print((self.time_left) * ' ', end='' )
        print(f'] {25 - self.time_left} / 25')

    def start(self):
        self.time_left = self.timeout

        while  self.time_left >= 0:
            self._display_status()

            time.sleep(60)
            self.time_left -= 1

        print("\n\n\n          Well done!! Now go and get a reward")

        logger.info("  end: " + sys.argv[1])
        logger.info(" ")

if __name__ == '__main__':
    pomodoro = Pomodoro(25)
    pomodoro.start()
