"""
"""

# Standard library imports
import os
import time
# Third party imports
# Local application/library imports
from hotkey.error import Error


class Utils_error(Error):
    pass


def clear_screen():

    def clear_nt():
        os.system('cls')

    def clear_posix():
        os.system('clear')

    if os.name == 'nt':
        clear_nt()
    elif os.name == 'posix':
        clear_posix()
    else:
        raise Utils_error("Unsupported OS.")


if __name__ == "__main__":

    print('this is', __name__)
    time.sleep(1.0)

    clear_screen()
    print('screen was cleared')
    time.sleep(1.0)
