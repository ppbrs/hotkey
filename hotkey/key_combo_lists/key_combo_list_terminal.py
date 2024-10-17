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
            ),
            # alt + f
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="f"),
                legend=[
                    "Move the cursor one word right -->.",
                ],
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
            ),
            # ctrl + b
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="b"),
                legend=[
                    "Move the cursor one character left <--.",
                ],
            ),
            # ctrl + c
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="c"),
                legend=[
                    "Command-line interfaces: cancel, abort, interrupt",
                ],
            ),
            # ctrl + d
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="d"),
                legend=[
                    "Delete a character under the cursor.",
                    "Python interpreter: exit",
                ],
            ),
            # ctrl + e
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="e"),
                legend=[
                    "Move the cursor to end of line -->.",
                ],
            ),
            # ctrl + f
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="f"),
                legend=[
                    "Move the cursor one character to the right -->.",
                ],
            ),
            # ctrl + k
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="k"),
                legend=[
                    "Clear up to the end -->.",
                ],
            ),
            # ctrl + l
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="l"),
                legend=[
                    "Clear the screen.",
                ],
            ),
            # ctrl + p
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="p"),
                legend=[
                    "Pull in the previous command.",
                ],
            ),
            # ctrl + q
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="q"),
                legend=[
                    "Resume transmission.",
                ],
            ),
            # ctrl + r
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="r"),
                legend=[
                    "Search in history: go to the previous result "
                    "(i.e. search backward, reverse-i-search).",
                ],
            ),
            # ctrl + s
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="s"),
                legend=[
                    "Search in history: go to the following result "
                    "(i.e. search forward, i-search).",
                ],
            ),
            # ctrl + u
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="u"),
                legend=[
                    "Clear up to the beginning <--.",
                ],
            ),
            # ctrl + w
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="w"),
                legend=[
                    "Clear the last word <--.",
                ],
            ),
            # ctrl + z
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="z"),
                legend=[
                    "Linux: suspend current process and put it to background (then `fg`).",
                ],
            ),
            # ctrl + 0
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="0"),
                legend=[
                    "Zoom Reset.",
                ],
            ),
            # # ctrl + -
            # KeyCombo(
            #     mode=Mode(ctrl=True),
            #     key=Key(specific="-"),
            #     legend=[
            #         "Zoom Out.",
            #     ],
            # ),
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
            ),
            # ctrl + shift + n
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="n"),
                legend=[
                    "Open a new terminal window (from within a terminal).",
                ],
            ),
            # ctrl + shift + t
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="t"),
                legend=[
                    "Open a new terminal tab (from within a terminal).",
                ],
            ),
            # ctrl + shift + v
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="v"),
                legend=[
                    "Paste from clipboard.",
                ],
            ),
            # ctrl + shift + =
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="="),
                legend=[
                    "Zoom In.",
                ],
            ),
            # ctrl + shift + w
            # KeyCombo(mode=Mode(ctrl=True, shift=True), key=Key(specific="w"),
            #           legend=["QTerminal: close current tab", ],
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
            ),
            # ---------------------------------------------------------------------
            # ctrl-gr + ...
            # ---------------------------------------------------------------------
            # ---------------------------------------------------------------------
            # win + ...
            # ---------------------------------------------------------------------
            # ---------------------------------------------------------------------
        ]
