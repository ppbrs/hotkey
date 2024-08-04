"""KeyCombo class."""
import logging
import threading

import keyboard

from hotkey.key import Key
from hotkey.mode import Mode

_logger = logging.getLogger(__name__)


class KeyCombo:
    """Set keyboard hooks and compare pressed combos with expected."""

    def __init__(
        self, mode: Mode, key: Key, legend: list[str], weight: int
    ):
        """
        :param mode: Object of class Mode.
        :param key: Object of class Key.
        :param legend: Iterable of description strings.
        """

        self.mode = mode
        self.key = key
        self.legend = legend
        self.weight = weight
        assert (self.weight > 0), "Bad weight"

        self.result: bool | None = None
        self.sem: threading.Semaphore
        self.mode_actual: Mode

    def __repr__(self) -> str:

        res = str(self.mode)
        if res != "":
            res += " + "
        res += str(self.key)
        return "`" + res + "`"

    def wait(self) -> bool | None:
        """
        Returns:
            True: expected combo was pressed
            False: wrong combo was pressed
            None: quit-request was pressed
        """

        self.sem = threading.Semaphore(0)
        self.mode_actual = Mode()  # Empty mode

        if __name__ != "__main__":
            hook = keyboard.hook(callback=self.callback, suppress=True)
        else:
            pass  # Do nothing; this branch is for testing.

        self.sem.acquire()

        if __name__ != "__main__":
            keyboard.unhook(remove=hook)
        else:
            pass  # Do nothing; this branch is for testing.

        self.sem.release()
        return self.result

    def callback(
        self,
        event: keyboard.KeyboardEvent
    ) -> None:
        """
        Process a keyboard event.

        Event is an object that at least has "name" and "event_type" attributes.
        """

        if event.event_type not in ("down", "up", ):
            raise TypeError("Unexpected event type: neither `down` nor `up`")

        _logger.debug("KeyCombo.callback: event=%s", event)
        if event.name in Mode.modifier_keys:
            self.mode_actual.update(
                is_set=(event.event_type == "down"), modifier_key=event.name)
        elif event.event_type == "down":
            event_key = Key(specific=event.name)
            key_match = event_key == self.key

            mode_match = self.mode_actual == self.mode

            quit_request = self._is_quit_request(mode=self.mode_actual, key=event_key)
            good = (key_match and mode_match)
            bad = not (key_match and mode_match)

            if good:
                self.result = True
                self.sem.release()
            elif quit_request:
                print("quit request (C+c)")
                self.result = None
                self.sem.release()
            elif bad:
                print(self.mode_actual, event.name)
                self.result = False
                self.sem.release()
            else:
                raise ValueError("Shouldn't get here.")

    @staticmethod
    def _is_quit_request(mode: Mode, key: Key) -> bool:
        """Check if Ctrl+C is pressed."""
        return mode == Mode(ctrl=True) and key == Key(specific="c")  # type: ignore[no-any-return]
