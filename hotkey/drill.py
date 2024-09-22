"""Drill class."""

import logging
import random
import time

from hotkey.key_combo import KeyCombo
from hotkey.utils import clear_screen

_logger = logging.getLogger(__name__)


class Drill:  # pylint: disable=too-few-public-methods
    """A namespace that contains the run function."""

    HINT_AFTER_NTH_ATTEMPT = 3  # Start showing hints after 3rd attempt

    def __init__(self) -> None:
        """Initialize a drill."""
        self.quit_request = False

    def run(self, count: int, key_combo_list: list[KeyCombo]) -> None:
        """
        Run a drill.

        :param count: Number of iterations to run.
        :param key_combo_list: an iterable of `KeyCombo` to choose from randomly.
        """
        if not key_combo_list:
            msg = "key_combo_list is empty"
            raise ValueError(msg)

        for i in range(count):
            clear_screen()
            print(f"Drill {(i + 1)} of {count}:\n")

            # Set types of specific combos in this drill
            key_combo = random.choices(key_combo_list)[0]

            has_legend = (key_combo.legend is not None) and (len(key_combo.legend) > 0)
            if has_legend:
                self._show_legend(key_combo=key_combo)

            print("")
            self._wait_for_key_combo(key_combo=key_combo)

            print()

            del key_combo
            if self.quit_request:
                break

        clear_screen()
        print("\ndone, quitting ...")
        time.sleep(1.0)

    def _show_legend(
        self,
        key_combo: KeyCombo,
    ) -> None:
        print("Legend:")
        legend = list(key_combo.legend)
        random.shuffle(legend)
        print(f"\t{legend[0]}")

    def _wait_for_key_combo(
        self,
        key_combo: KeyCombo,
    ) -> None:
        attempt = 0
        success = False
        cnt_mistakes = 0
        while not success:
            attempt += 1
            if attempt < self.HINT_AFTER_NTH_ATTEMPT:
                print(f"#{attempt}: Waiting:")
            else:
                print(f"#{attempt}: Waiting for {key_combo}:")
            success = key_combo.wait()
            if success is True:  # correct combo was pressed
                print("good")
            elif success is False:  # wrong combo was pressed
                print("mistake, try again")
                cnt_mistakes += 1
            elif success is None:  # quit request was pressed
                print("Quit request was pressed")
                self.quit_request = True
                break
            else:
                msg = "Shouldn't get here."
                raise RuntimeError(msg)
            try:
                time.sleep(0.1)
            except KeyboardInterrupt:
                time.sleep(1.0)
            print("")
