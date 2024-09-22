"""Configure the hotkeys that are related to linux terminal and bash."""

from hotkey.key import Key
from hotkey.key_combo import KeyCombo
from hotkey.key_combo_lists.key_combo_list_interface import KeyComboListInterface
from hotkey.mode import Mode

# "noqa" in class's first line silences the error that I cannot explain:
# Class cannot subclass "KeyComboListInterface" (has type "Any")  [misc] [mypy]

class KeyComboListTerminal(KeyComboListInterface):  # pylint: disable=too-few-public-methods # noqa
    """Data class that holds specific hotkeys."""

    LEGEND_PREFIX = "TERMINAL"

    def _get(self) -> list[KeyCombo]:
        return [
            # ---------------------------------------------------------------------
            # alt + ...
            # ---------------------------------------------------------------------
            # alt + b
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="b"),
                legend=[
                    "Move the cursor one word left <--.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # alt + f
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="f"),
                legend=[
                    "Move the cursor one word right -->.",
                ],
                weight=self.WEIGHT_NORMAL,
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
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="a"),
                legend=[
                    "Move the cursor to the start of the line <--.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + b
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="b"),
                legend=[
                    "Move the cursor one character left <--.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + c
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="c"),
                legend=[
                    "Command-line interfaces: cancel, abort, interrupt",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + d
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="d"),
                legend=[
                    "Delete a character under the cursor.",
                    "Python interpreter: exit",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + e
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="e"),
                legend=[
                    "Move the cursor to end of line -->.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + f
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="f"),
                legend=[
                    "Move the cursor one character to the right -->.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + k
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="k"),
                legend=[
                    "Clear up to the end -->.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + l
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="l"),
                legend=[
                    "Clear the screen.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + p
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="p"),
                legend=[
                    "Pull in the previous command.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + q
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="q"),
                legend=[
                    "Resume transmission.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + r
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="r"),
                legend=[
                    "Search in history: go to the previous result "
                    "(i.e. search backward, reverse-i-search).",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + s
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="s"),
                legend=[
                    "Search in history: go to the following result "
                    "(i.e. search forward, i-search).",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + u
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="u"),
                legend=[
                    "Clear up to the beginning <--.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + w
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="w"),
                legend=[
                    "Clear the last word <--.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + z
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="z"),
                legend=[
                    "Linux: suspend current process and put it to background (then `fg`).",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ---------------------------------------------------------------------
            # shift + ...
            # ---------------------------------------------------------------------
            # ---------------------------------------------------------------------
            # ctrl + shift + ...
            # ---------------------------------------------------------------------
            # ctrl + shift + c
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="c"),
                legend=[
                    "Copy the selection to clipboard.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + shift + n
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="n"),
                legend=[
                    "Open a new terminal window (from within a terminal).",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + shift + t
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="t"),
                legend=[
                    "Open a new terminal tab (from within a terminal).",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + shift + v
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="v"),
                legend=[
                    "Paste from clipboard.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + shift + w
            # KeyCombo(mode=Mode(ctrl=True, shift=True), key=Key(specific="w"),
            #           legend=["QTerminal: close current tab", ],
            #           weight=self.WEIGHT_NORMAL,
            #           ),
            # ---------------------------------------------------------------------
            # shift + alt + ...
            # ---------------------------------------------------------------------
            # ---------------------------------------------------------------------
            # ctrl + alt + ...
            # ---------------------------------------------------------------------
            # ctrl + alt + T
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="t"),
                legend=[
                    "Start a new terminal (from anywhere in Linux).",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ---------------------------------------------------------------------
            # ctrl-gr + ...
            # ---------------------------------------------------------------------
            # ---------------------------------------------------------------------
            # win + ...
            # ---------------------------------------------------------------------
            # ---------------------------------------------------------------------
        ]
