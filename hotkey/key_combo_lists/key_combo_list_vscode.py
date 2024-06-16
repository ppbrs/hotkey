""" Configure the hotkeys that are specific to sublime-text.
"""
from hotkey.key import Key
from hotkey.key_combo import Key_combo
from hotkey.key_combo_lists.key_combo_list_interface import KeyComboListInterface
from hotkey.mode import Mode


class KeyComboListVscode(KeyComboListInterface):
    """ Data class that holds specific hotkeys. """
    LEGEND_PREFIX = "VS CODE"

    def _get(self) -> list[Key_combo]:
        return [

            # ---------------------------------------------------------------------
            # alt + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # alt_gr + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # standalone keys
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # ctrl + ...
            # ---------------------------------------------------------------------
            # ctrl + `
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="`"),
                      legend=["Toggle the integrated Terminal.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + b
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="b"),
                      legend=["Toggle the sidebar.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),

            # ---------------------------------------------------------------------
            # shift + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # ctrl + shift + ...
            # ---------------------------------------------------------------------
            # ctrl + shift + d
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="d"),
                      legend=["Open \"Debug\" view.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + shift + e
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="e"),
                      legend=["Open \"Explore\" view.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + shift + o
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="o"),
                      legend=["Go to symbol ...", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + shift + y
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="y"),
                      legend=["Toggle \"Debug Console\".", ],
                      weight=self.WEIGHT_NORMAL,
                      ),

            # ---------------------------------------------------------------------
            # shift + alt + ...
            # ---------------------------------------------------------------------
            # shift + alt + tab
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
