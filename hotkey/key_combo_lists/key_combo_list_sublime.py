""" Configure the hotkeys that are specific to sublime-text.
"""
from hotkey.key import Key
from hotkey.key_combo import Key_combo
from hotkey.key_combo_lists.key_combo_list_interface import KeyComboListInterface
from hotkey.mode import Mode


class KeyComboListSublime(KeyComboListInterface):
    """ Data class that holds specific hotkeys. """
    LEGEND_PREFIX = "SUBLIME"

    def _get(self) -> list[Key_combo]:
        return [

            # ---------------------------------------------------------------------
            # alt + ...
            # ---------------------------------------------------------------------
            # alt + b
            Key_combo(mode=Mode(alt=True), key=Key(specific="b"),
                      legend=["[CUSTOM] Cancel the running build.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # alt + c
            Key_combo(mode=Mode(alt=True), key=Key(specific="c"),
                      legend=["FIND dialog: Toggle case sensitive search.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # alt + d
            Key_combo(mode=Mode(alt=True), key=Key(specific="d"),
                      legend=["[CUSTOM] Delete the character under (=to the right) the cursor.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # alt + r
            Key_combo(mode=Mode(alt=True), key=Key(specific="r"),
                      legend=["FIND dialog: Toggle regex search.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # alt + z
            Key_combo(mode=Mode(alt=True), key=Key(specific="z"),
                      legend=["[CUSTOM] Word wrap. (Also works in VS Code)", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # alt + enter
            Key_combo(mode=Mode(alt=True), key=Key(enter=True),
                      legend=[
                          "FIND dialog: Select all."],
                      weight=self.WEIGHT_NORMAL,
                      ),

            # ---------------------------------------------------------------------
            # alt_gr + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # standalone keys
            # ---------------------------------------------------------------------
            # tab
            Key_combo(mode=Mode(), key=Key(tab=True),
                      legend=["auto-completion: Choose the highlighted variant.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),

            # ---------------------------------------------------------------------
            # ctrl + ...
            # ---------------------------------------------------------------------
            # ctrl + +
            # ---------------------------------------------------------------------
            # Key_combo(mode=Mode(ctrl=True), key=Key(specific="+"),
            #           legend=["Sublime+: zoom in", ],
            #           weight=self.WEIGHT_NORMAL,
            #           ),
            # ctrl + -
            # Key_combo(mode=Mode(ctrl=True), key=Key(specific="-"),
            #           legend=["Sublime+: zoom out", ],
            #           weight=self.WEIGHT_NORMAL,
            #           ),
            # ctrl + /
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="/"),
                      legend=["Comment/Uncomment current line.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + space
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="space"),
                      legend=["auto-completion: Show variants.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + 0
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="0"),
                      legend=["Focus on sidebar.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + 1
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="1"),
                      legend=["Focus on 1st column.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + 2
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="2"),
                      legend=["Focus on 2nd column.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + b
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="b"),
                      legend=["Build.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + d
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="d"),
                      legend=["Select next.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + g
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="g"),
                      legend=["Go to line number ...", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + m
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="m"),
                      legend=["Jump to the matching bracket.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + p
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="p"),
                      legend=["Go to file ...", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + t
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="t"),
                      legend=["Swap two selections.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),

            # ---------------------------------------------------------------------
            # shift + ...
            # ---------------------------------------------------------------------
            # shift + enter
            Key_combo(mode=Mode(shift=True), key=Key(enter=True),
                      legend=[
                          "FIND dialog: Search backwards."],
                      weight=self.WEIGHT_NORMAL,
                      ),

            # ---------------------------------------------------------------------
            # ctrl + shift + ...
            # ---------------------------------------------------------------------
            # ctrl + shift + 1
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="1"),
                      legend=["Move the file under focus to the 1st column.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + shift + 2
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="2"),
                      legend=["Move the file under focus to the 2nd column.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + shift + b
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="b"),
                      legend=["Build with ...", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + shift + c
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="c"),
                      legend=["[CUSTOM] Copy file path", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + shift + d
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="d"),
                      legend=["Duplicate the line", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + shift + k
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="k"),
                      legend=["Delete the line. (Also works in VS Code)", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + shift + m
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="m"),
                      legend=["Select everything inside the brackets, braces,parentheses.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + shift + o
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="o"),
                      legend=["[CUSTOM] Open the containing directory in file explorer.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + shift + p
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="p"),
                      legend=["commands", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + shift + y
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="y"),
                      legend=["[CUSTOM] Reveal the file in the side bar.", ],
                      weight=self.WEIGHT_NORMAL,
                      ),
            # ctrl + shift + /
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="/"),
                      legend=["Comment/Uncomment a selected block.", ],
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
