""" Configure the hotkeys that are related to linux terminal and bash.
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


class KeyComboListTerminal(KeyComboListInterface):
    """ Data class that holds specific hotkeys. """
    LEGEND_PREFIX = "TERMINAL"

    def _get(self, log: Log) -> list[Key_combo]:
        return [

            # ---------------------------------------------------------------------
            # alt + ...
            # ---------------------------------------------------------------------
            # alt + b
            Key_combo(mode=Mode(alt=True), key=Key(specific="b"),
                      legend=["Move the cursor one word left <--.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # alt + f
            Key_combo(mode=Mode(alt=True), key=Key(specific="f"),
                      legend=["Move the cursor one word right -->.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),

            # ---------------------------------------------------------------------
            # alt_gr + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # standalone keys
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # ctrl + ...
            # ---------------------------------------------------------------------
            # ctrl + +
            # ---------------------------------------------------------------------
            # ctrl + a
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="a"),
                      legend=["Move the cursor to the start of the line <--.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + b
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="b"),
                      legend=["Move the cursor one character left <--.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + c
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="c"),
                      legend=["Command-line interfaces: cancel, abort, interrupt", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + d
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="d"),
                      legend=["Delete a character under the cursor.",
                              "Python interpreter: exit", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + e
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="e"),
                      legend=["Move the cursor to end of line -->.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + f
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="f"),
                      legend=["Move the cursor one character to the right -->.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + k
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="k"),
                      legend=["Clear up to the end -->.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + l
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="l"),
                      legend=["Clear the screen.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + p
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="p"),
                      legend=["Pull in the previous command.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + q
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="q"),
                      legend=["Resume transmission.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + r
            Key_combo(
                mode=Mode(ctrl=True), key=Key(specific="r"),
                legend=["Start searching in history.",
                        "Search in history: go to the previous result (i.e. search backward).", ],
                weight=self.WEIGHT_NORMAL,
                log=log),
            # ctrl + s
            Key_combo(
                mode=Mode(ctrl=True), key=Key(specific="s"),
                legend=["Search in history: go to the following result (i.e. search forward).", ],
                weight=self.WEIGHT_NORMAL,
                log=log),
            # ctrl + u
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="u"),
                      legend=["Clear up to the beginning <--.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + w
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="w"),
                      legend=["Clear the last word <--.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + z
            Key_combo(
                mode=Mode(ctrl=True), key=Key(specific="z"),
                legend=["Linux: suspend current process and put it to background (then `fg`).", ],
                weight=self.WEIGHT_NORMAL,
                log=log),

            # ---------------------------------------------------------------------
            # shift + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # ctrl + shift + ...
            # ---------------------------------------------------------------------
            # ctrl + shift + c
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="c"),
                      legend=["Copy the selection to clipboard.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + shift + n
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="n"),
                      legend=["Open a new terminal window (from within a terminal).", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + shift + t
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="t"),
                      legend=["Open a new terminal tab (from within a terminal).", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + shift + v
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="v"),
                      legend=["Paste from clipboard.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + shift + w
            # Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="w"),
            #           legend=["QTerminal: close current tab", ],
            #           weight=self.WEIGHT_NORMAL,
            #           log=log
            #           ),

            # ---------------------------------------------------------------------
            # shift + alt + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # ctrl + alt + ...
            # ---------------------------------------------------------------------
            # ctrl + alt + T
            Key_combo(mode=Mode(ctrl=True, alt=True), key=Key(specific="t"),
                      legend=["Start a new terminal (from anywhere in Linux).", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),

            # ---------------------------------------------------------------------
            # ctrl-gr + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # win + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
        ]
