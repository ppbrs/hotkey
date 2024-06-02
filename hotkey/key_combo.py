"""

"""
import threading

import keyboard
from pybp.log import Log

from hotkey.key import Key
from hotkey.mode import Mode


class Key_combo:

    def __init__(self, mode: Mode, key: Key, log: Log, legend: list[str], weight: int):
        """

        Args:
            mode: Object of class Mode.
            key: Object of class Key.
            legend: Iterable of description string.

        """

        self.mode = mode
        self.key = key
        self.legend = legend
        self.weight = weight
        self.log = log
        assert (self.weight > 0), "Bad weight"

    def __del__(self):
        pass

    def __repr__(self):

        res = str(self.mode)
        if res != '':
            res += ' + '
        res += str(self.key)
        return '`' + res + '`'

    def callback(self, event):
        """Process keyboard event.

        event.name
        event.type = keyboard.KEY_DOWN, keyboard.KEY_UP
        """

        if event.event_type not in ('down', 'up', ):
            raise TypeError('Unexpected event type: neither `down` nor `up`')

        self.log.debug(f'Key_combo.callback: event={str(event)}')
        modes = ('alt', 'left alt',
                 'alt gr', 'right alt',
                 'ctrl', 'right ctrl', 'left ctrl',
                 'shift', 'right shift', 'left shift',
                 'left windows',
                 )
        if event.name in modes:
            # print(event.name)
            self.mode_actual.update(is_set=(event.event_type == 'down'),
                                    name=event.name)
        elif (event.event_type == 'down'):

            event_key = Key(specific=event.name)
            key_match = (event_key == self.key)

            mode_match = self.mode_actual.is_expected(expected=self.mode)

            quit_request = self._is_quit_request(mode=self.mode_actual, key=event_key)
            good = (key_match and mode_match)
            bad = not (key_match and mode_match)

            if good:
                self.result = True
                self.sem.release()
            elif quit_request:
                print('quit request (C+c)')
                self.result = None
                self.sem.release()
            elif bad:
                print(self.mode_actual, event.name)
                self.result = False
                self.sem.release()
            else:
                raise Exception("Shouldn't get here.")

    @staticmethod
    def _is_quit_request(mode: Mode, key: Key) -> bool:
        """ Check if Ctrl+C is pressed.
        """
        return mode == Mode(ctrl=True) and key == Key(specific='c')

    def wait(self) -> bool or None:
        """
        Returns:
            True: expected combo was pressed
            False: wrong combo was pressed
            None: quit-request was pressed
        """

        self.sem = threading.Semaphore(0)
        self.mode_actual = Mode()

        if __name__ != '__main__':
            hook = keyboard.hook(callback=self.callback, suppress=True)

        self.sem.acquire()

        if __name__ != '__main__':
            keyboard.unhook(remove=hook)

        self.sem.release()
        return self.result
