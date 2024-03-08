"""
"""

# Standard library imports
import random
import time
# Third party imports
from pybp.log import Log
# Local application/library imports
from hotkey.utils import (clear_screen, )
from hotkey.key_combo import Key_combo


class Drill():

    @staticmethod
    def run(count: int, key_combo_list: list[Key_combo], log: Log):
        """
        :param count: Number of iterations to run.
        :param key_combo_list: an iterable of `Key_combo` to choose from randomly.
        :param log:
        """
        if len(key_combo_list) < 1:
            raise ValueError('key_combo_list is empty')

        for i in range(count):
            clear_screen()
            print(f'Drill {(i + 1)} of {count}:')
            print()

            # Set types of specific combos in this drill
            weights = [i.weight for i in key_combo_list]
            key_combo = random.choices(key_combo_list,
                                       weights=weights)[0]

            # Show legend:
            has_legend = (key_combo.legend is not None) and \
                         (len(key_combo.legend) > 0)
            if has_legend:
                print('Legend:')
                legend = list(key_combo.legend)
                random.shuffle(legend)
                print(f'    {legend[0]}')
            # Show weight:
            print(f'Weight = {key_combo.weight}')

            print('')
            attempt = 0
            success = False
            cnt_mistakes = 0
            quit_request = False
            while not success:
                attempt += 1
                quit_request = False
                if has_legend and (attempt < 3):
                    print(f'#{attempt}: Waiting:')
                else:
                    print(f'#{attempt}: Waiting for {key_combo}:')
                success = key_combo.wait()
                if success is True:  # correct combo was pressed
                    print('good')
                elif success is False:  # wrong combo was pressed
                    print('mistake, try again')
                    cnt_mistakes += 1
                elif success is None:  # quit request was pressed
                    print('Quit request was pressed')
                    quit_request = True
                    break
                else:
                    raise Exception("Shouldn't get here.")
                try:
                    time.sleep(0.1)
                except KeyboardInterrupt:
                    time.sleep(1.0)
                print('')

            print()

            del key_combo
            if quit_request:
                break

        clear_screen()
        print()
        print('done, quitting ...')
        time.sleep(1.0)


if __name__ == "__main__":
    pass
