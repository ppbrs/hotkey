"""
Drill specific hotkeys from the list.

Put the most frequent hotkeys to the list.
"""

# if not __package__:
#     import sys
#     import os
#     root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
#     sys.path.append(root_path)


# Standard library imports
import time
# Third party imports
from pybp.log import Log
# Local application imports
from hotkey.drill import Drill
from hotkey.key_combo_lists.key_combo_list_mix import KeyComboListMix
from hotkey.key_combo_lists.key_combo_list_sublime import KeyComboListSublime
from hotkey.key_combo_lists.key_combo_list_terminal import KeyComboListTerminal
from hotkey.key_combo_lists.key_combo_list_universal import KeyComboListUniversal
from hotkey.key_combo_lists.key_combo_list_vscode import KeyComboListVscode


def run():

    log = Log(console=False)
    # log = Log(fname=(__file__ + '.log'), level=Log.DEBUG, filemode='w', console=False)
    try:

        key_combo_list = []
        key_combo_list += KeyComboListMix().get(log=log)
        key_combo_list += KeyComboListSublime().get(log=log)
        key_combo_list += KeyComboListTerminal().get(log=log)
        key_combo_list += KeyComboListUniversal().get(log=log)
        key_combo_list += KeyComboListVscode().get(log=log)

        Drill.run(count=30,
                  key_combo_list=key_combo_list,
                  log=log)
    except Exception as e:
        log.error(f'{e.__class__.__name__}: {str(e)}')
        print('done, quitting ...')
        time.sleep(1)


if __name__ == "__main__":
    run()
