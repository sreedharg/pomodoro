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
        self.current_item = ""
        self.items_done = 0

    def _init_logger(self):
        logger.setLevel(logging.INFO)

        logfile_name = 'pomodoro.log'

        fh = logging.FileHandler(logfile_name)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        fh.setLevel(logging.DEBUG)

        logger.addHandler(fh)

    def _display_status(self):
        os.system('cls')
        print('\n\n\n         Busy with - ' + self.current_item)
        print('\n\n\n         [', end='')
        print((25 - self.time_left) * '*' , end='' )
        print((self.time_left) * ' ', end='' )
        print(f'] {25 - self.time_left} / 25')

    def start(self):
        os.system('cls')
        self.current_item = input("\n\n\n          Enter a short title of the work: ")
        logger.info("start: " + self.current_item)

        self.time_left = self.timeout

        while  self.time_left >= 0:
            self._display_status()

            time.sleep(60)
            self.time_left -= 1

        print("\n\n\n          Well done!! Now go and get a reward!! ")

        logger.info("  end: " + self.current_item)
        logger.info(" ")

        self.items_done += 1

    def relax(self):
        if self.items_done % 4 == 0:
            break_time = 25
        else:
            break_time = 5

        os.system('cls')
        print("\n\n\n          Taking a break for " + str(break_time) + " minutes")

        logger.info("Taking a break for " + str(break_time) + " minutes")
        time.sleep(break_time * 60)
        logger.info("Done with the break :)")


if __name__ == '__main__':
    pomodoro = Pomodoro(25)

    while True:
        pomodoro.start()
        pomodoro.relax()

        another_pom = input("Want to start another pomodoro? Y/N ")

        if another_pom in ['n', 'N']:
            print("          Done with pomodoing, Bye. :) ")
            break
