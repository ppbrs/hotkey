"""
Drill specific hotkeys from the list.

Put the most frequent hotkeys to the list.
"""

# if not __package__:
#     import sys
#     import os
#     root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
#     sys.path.append(root_path)

import logging
import pathlib
import time
from datetime import datetime

from hotkey.drill import Drill
from hotkey.key_combo_lists.key_combo_list_mix import KeyComboListMix
from hotkey.key_combo_lists.key_combo_list_sublime import KeyComboListSublime
from hotkey.key_combo_lists.key_combo_list_terminal import KeyComboListTerminal
from hotkey.key_combo_lists.key_combo_list_universal import KeyComboListUniversal
from hotkey.key_combo_lists.key_combo_list_vscode import KeyComboListVscode


def run():
    log_file = pathlib.Path(datetime.today().strftime("%Y%m%d.%H%M%S.log"))
    format = "%(asctime)s.%(msecs)03d %(levelname)-8s %(name)s: %(funcName)s: %(message)s"
    datefmt = "%H%M%S"
    logging.basicConfig(
        format=format, datefmt=datefmt,
        level=logging.DEBUG,
        filename=log_file, filemode="w",
    )
    logger = logging.getLogger(__name__)

    try:

        key_combo_list = []
        key_combo_list += KeyComboListMix().get()
        key_combo_list += KeyComboListSublime().get()
        key_combo_list += KeyComboListTerminal().get()
        key_combo_list += KeyComboListUniversal().get()
        key_combo_list += KeyComboListVscode().get()

        Drill.run(
            count=30,
            key_combo_list=key_combo_list)
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {str(e)}')
        print('done, quitting ...')
        time.sleep(1)


if __name__ == "__main__":
    run()
