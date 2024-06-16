""" Configure the hotkeys that are universal for many applications and
operating systems.
"""
from hotkey.key import Key
from hotkey.key_combo import Key_combo
from hotkey.key_combo_lists.key_combo_list_interface import KeyComboListInterface
from hotkey.mode import Mode


class KeyComboListUniversal(KeyComboListInterface):
    """ Data class that holds specific hotkeys. """
    LEGEND_PREFIX = "UNIVERSAL"

    def _get(self) -> list[Key_combo]:
        return [

            # ---------------------------------------------------------------------
            # alt + ...
            # ---------------------------------------------------------------------
            # alt + space
            Key_combo(mode=Mode(alt=True), key=Key(specific="space"),
                      legend=["Windows: Open the window menu.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # alt + tab
            Key_combo(mode=Mode(alt=True), key=Key(tab=True),
                      legend=["Windows: Task swtcher forward. -->", ],
                      weight=self.WEIGHT_NORMAL,
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
                      ),
            # tab
            Key_combo(mode=Mode(), key=Key(tab=True),
                      legend=["Press TAB key."],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # enter
            Key_combo(mode=Mode(), key=Key(enter=True),
                      legend=["Press ENTER key."],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # del
            Key_combo(mode=Mode(), key=Key(delete=True),
                      legend=["Press DEL key."],
                      weight=self.WEIGHT_NORMAL,
                      ),

            # ---------------------------------------------------------------------
            # ctrl + ...
            # ---------------------------------------------------------------------
            # ctrl + a
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="a"),
                      legend=["Select all.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + b
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="b"),
                      legend=["Boldify.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + c
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="c"),
                      legend=["Copy a selection to the clipboard.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + f
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="f"),
                      legend=["Chrome,etc: Start searching on the page.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + g
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="g"),
                      legend=["Chrome,etc: Find NEXT on the page.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + i
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="i"),
                      legend=["Italicize.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + q
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="q"),
                      legend=["Linux: Close the application.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + s
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="s"),
                      legend=["Save.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + u
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="u"),
                      legend=["Underline.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + v
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="v"),
                      legend=["Paste from the clipboard.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + w
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="w"),
                      legend=["Multitab: Close the current tab.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + x
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="x"),
                      legend=["Cut to clipboard.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + y
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="y"),
                      legend=["Re-do.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + z
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="z"),
                      legend=["Undo.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + tab
            Key_combo(mode=Mode(ctrl=True), key=Key(tab=True),
                      legend=["Multitab: Switch to the next tab. -->", ],
                      weight=self.WEIGHT_NORMAL,
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
                      ),
            # ctrl + shift + g
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="g"),
                      legend=["Chrome,etc: Find PREVIOUS on the page.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),

            # ---------------------------------------------------------------------
            # shift + alt + ...
            # ---------------------------------------------------------------------
            # shift + alt + tab
            Key_combo(mode=Mode(shift=True, alt=True), key=Key(tab=True),
                      legend=["Windows: Task swtcher backward. <--", ],
                      weight=self.WEIGHT_NORMAL,
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
