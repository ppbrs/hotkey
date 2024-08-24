"""
Drill specific hotkeys from the provided lists.
"""

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


def run() -> None:
    """Run hotkey drills from all lists."""
    log_file = pathlib.Path(datetime.today().strftime("%Y%m%d.%H%M%S.log"))
    log_fmt = "%(asctime)s.%(msecs)03d %(levelname)-8s %(name)s: %(funcName)s: %(message)s"
    date_fmt = "%H%M%S"
    logging.basicConfig(
        format=log_fmt,
        datefmt=date_fmt,
        level=logging.DEBUG,
        filename=log_file,
        filemode="w",
    )
    logger = logging.getLogger(__name__)

    try:
        key_combo_list = []
        key_combo_list += KeyComboListMix().get()
        key_combo_list += KeyComboListSublime().get()
        key_combo_list += KeyComboListTerminal().get()
        key_combo_list += KeyComboListUniversal().get()
        key_combo_list += KeyComboListVscode().get()

        Drill.run(count=30, key_combo_list=key_combo_list)
    except Exception as e:  # pylint: disable=broad-exception-caught
        logger.error("%s: %s", e.__class__.__name__, e)
        print(f"{e.__class__.__name__}: Done, quitting ...")
        time.sleep(1)


if __name__ == "__main__":
    run()
