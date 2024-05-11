""" Configure the hotkeys that are universal for many applications and
operating systems.
"""
# pylint: disable=import-error

# Standard library imports
# Third party imports
from pybp.log import Log
# Local application imports
from hotkey.key_combo_lists.key_combo_list_interface import KeyComboListInterface
from hotkey.key_combo import Key_combo
from hotkey.mode import Mode
from hotkey.key import Key


class KeyComboListUniversal(KeyComboListInterface):
    """ Data class that holds specific hotkeys. """
    LEGEND_PREFIX = "UNIVERSAL"

    def _get(self, log: Log) -> list[Key_combo]:
        return [

            # ---------------------------------------------------------------------
            # alt + ...
            # ---------------------------------------------------------------------
            # alt + space
            Key_combo(mode=Mode(alt=True), key=Key(specific="space"),
                      legend=["Windows: Open the window menu.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # alt + tab
            Key_combo(mode=Mode(alt=True), key=Key(tab=True),
                      legend=["Windows: Task swtcher forward. -->", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),

            # ---------------------------------------------------------------------
            # alt_gr + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # standalone keys
            # ---------------------------------------------------------------------
            # esc
            Key_combo(mode=Mode(), key=Key(esc=True),
                      legend=["Press ESC key.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # tab
            Key_combo(mode=Mode(), key=Key(tab=True),
                      legend=["Press TAB key."],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # enter
            Key_combo(mode=Mode(), key=Key(enter=True),
                      legend=["Press ENTER key."],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # del
            Key_combo(mode=Mode(), key=Key(delete=True),
                      legend=["Press DEL key."],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),

            # ---------------------------------------------------------------------
            # ctrl + ...
            # ---------------------------------------------------------------------
            # ctrl + a
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="a"),
                      legend=["Select all.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + b
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="b"),
                      legend=["Boldify.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + c
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="c"),
                      legend=["Copy a selection to the clipboard.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + f
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="f"),
                      legend=["Chrome,etc: Start searching on the page.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + g
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="g"),
                      legend=["Chrome,etc: Find NEXT on the page.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + i
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="i"),
                      legend=["Italicize.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + q
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="q"),
                      legend=["Linux: Close the application.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + s
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="s"),
                      legend=["Save.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + u
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="u"),
                      legend=["Underline.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + v
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="v"),
                      legend=["Paste from the clipboard.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + w
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="w"),
                      legend=["Multitab: Close the current tab.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + x
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="x"),
                      legend=["Cut to clipboard.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + y
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="y"),
                      legend=["Re-do.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + z
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="z"),
                      legend=["Undo.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + tab
            Key_combo(mode=Mode(ctrl=True), key=Key(tab=True),
                      legend=["Multitab: Switch to the next tab. -->", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),

            # ---------------------------------------------------------------------
            # shift + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # ctrl + shift + ...
            # ---------------------------------------------------------------------
            # ctrl + shift + tab
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(tab=True),
                      legend=["Multitab: Switch to the previous tab. <--", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + shift + g
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="g"),
                      legend=["Chrome,etc: Find PREVIOUS on the page.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),

            # ---------------------------------------------------------------------
            # shift + alt + ...
            # ---------------------------------------------------------------------
            # shift + alt + tab
            Key_combo(mode=Mode(shift=True, alt=True), key=Key(tab=True),
                      legend=["Windows: Task swtcher backward. <--", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),

            # ---------------------------------------------------------------------
            # ctrl + alt + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # ctrl-gr + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # win + ...
            # ---------------------------------------------------------------------

        ]
