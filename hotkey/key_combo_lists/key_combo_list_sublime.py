"""Configure the hotkeys that are specific to sublime-text."""

from hotkey.key import Key
from hotkey.key_combo import KeyCombo
from hotkey.key_combo_lists.key_combo_list_interface import KeyComboListInterface
from hotkey.mode import Mode

# "noqa" in class's first line silences the error that I cannot explain:
# Class cannot subclass "KeyComboListInterface" (has type "Any")  [misc] [mypy]

class KeyComboListSublime(KeyComboListInterface):  # pylint: disable=too-few-public-methods # noqa
    """Data class that holds specific hotkeys."""

    LEGEND_PREFIX = "SUBLIME"

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
                    "CUSTOM: Cancel the running build.",
                ],
            ),
            # alt + c
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="c"),
                legend=[
                    "FIND dialog: Toggle case sensitive search.",
                ],
            ),
            # alt + d
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="d"),
                legend=[
                    "CUSTOM: Delete the character under (=to the right) the cursor.",
                ],
            ),
            # alt + r
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="r"),
                legend=[
                    "FIND dialog: Toggle regex search.",
                ],
            ),
            # alt + z
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="z"),
                legend=[
                    "CUSTOM: Word wrap. (Also works in VS Code)",
                ],
            ),
            # alt + enter
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(enter=True),
                legend=["FIND dialog: Select all."],
            ),
            # ---------------------------------------------------------------------
            # alt_gr + ...
            # ---------------------------------------------------------------------
            # ---------------------------------------------------------------------
            # standalone keys
            # ---------------------------------------------------------------------
            # tab
            KeyCombo(
                mode=Mode(),
                key=Key(tab=True),
                legend=[
                    "auto-completion: Choose the highlighted variant.",
                ],
            ),
            # ---------------------------------------------------------------------
            # ctrl + ...
            # ---------------------------------------------------------------------
            # ctrl + +
            # ---------------------------------------------------------------------
            # KeyCombo(mode=Mode(ctrl=True), key=Key(specific="+"),
            #           legend=["Sublime+: zoom in", ],
            #           ),
            # ctrl + -
            # KeyCombo(mode=Mode(ctrl=True), key=Key(specific="-"),
            #           legend=["Sublime+: zoom out", ],
            #           ),
            # ctrl + /
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="/"),
                legend=[
                    "Comment/Uncomment current line.",
                ],
            ),
            # ctrl + space
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="space"),
                legend=[
                    "auto-completion: Show variants.",
                ],
            ),
            # ctrl + 0
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="0"),
                legend=[
                    "Focus on sidebar.",
                ],
            ),
            # ctrl + 1
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="1"),
                legend=[
                    "Focus on 1st column.",
                ],
            ),
            # ctrl + 2
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="2"),
                legend=[
                    "Focus on 2nd column.",
                ],
            ),
            # ctrl + b
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="b"),
                legend=[
                    "Build.",
                ],
            ),
            # ctrl + d
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="d"),
                legend=[
                    "Select next.",
                ],
            ),
            # ctrl + g
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="g"),
                legend=[
                    "Go to line number ...",
                ],
            ),
            # ctrl + m
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="m"),
                legend=[
                    "Jump to the matching bracket.",
                ],
            ),
            # ctrl + p
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="p"),
                legend=[
                    "Go to file ...",
                ],
            ),
            # ctrl + t
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="t"),
                legend=[
                    "Swap two selections.",
                ],
            ),
            # ---------------------------------------------------------------------
            # shift + ...
            # ---------------------------------------------------------------------
            # shift + enter
            KeyCombo(
                mode=Mode(shift=True),
                key=Key(enter=True),
                legend=["FIND dialog: Search backwards."],
            ),
            # ---------------------------------------------------------------------
            # ctrl + shift + ...
            # ---------------------------------------------------------------------
            # ctrl + shift + 1
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="1"),
                legend=[
                    "Move the file under focus to the 1st column.",
                ],
            ),
            # ctrl + shift + 2
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="2"),
                legend=[
                    "Move the file under focus to the 2nd column.",
                ],
            ),
            # ctrl + shift + b
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="b"),
                legend=[
                    "Build with ...",
                ],
            ),
            # ctrl + shift + c
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="c"),
                legend=[
                    "CUSTOM: Copy file path",
                ],
            ),
            # ctrl + shift + d
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="d"),
                legend=[
                    "Duplicate the line",
                ],
            ),
            # ctrl + shift + k
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="k"),
                legend=[
                    "Delete the line. (Also works in VS Code)",
                ],
            ),
            # ctrl + shift + m
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="m"),
                legend=[
                    "Select everything inside the brackets, braces,parentheses.",
                ],
            ),
            # ctrl + shift + o
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="o"),
                legend=[
                    "CUSTOM: Open the containing directory in file explorer.",
                ],
            ),
            # ctrl + shift + p
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="p"),
                legend=[
                    "commands",
                ],
            ),
            # ctrl + shift + y
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="y"),
                legend=[
                    "CUSTOM: Reveal the file in the side bar.",
                ],
            ),
            # ctrl + shift + /
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="/"),
                legend=[
                    "Comment/Uncomment a selected block.",
                ],
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
