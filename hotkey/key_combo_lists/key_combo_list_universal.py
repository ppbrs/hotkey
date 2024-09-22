"""Configure the hotkeys that are universal for many applications and
operating systems.
"""

from hotkey.key import Key
from hotkey.key_combo import KeyCombo
from hotkey.key_combo_lists.key_combo_list_interface import KeyComboListInterface
from hotkey.mode import Mode

# "noqa" in class's first line silences the error that I cannot explain:
# Class cannot subclass "KeyComboListInterface" (has type "Any")  [misc] [mypy]

class KeyComboListUniversal(KeyComboListInterface):  # pylint: disable=too-few-public-methods # noqa
    """Data class that holds specific hotkeys."""

    LEGEND_PREFIX = "UNIVERSAL"

    def _get(self) -> list[KeyCombo]:
        return [
            # ---------------------------------------------------------------------
            # alt + ...
            # ---------------------------------------------------------------------
            # alt + space
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="space"),
                legend=[
                    "Windows: Open the window menu.",
                ],
            ),
            # alt + tab
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(tab=True),
                legend=[
                    "Windows: Task swtcher forward. -->",
                ],
            ),
            # ---------------------------------------------------------------------
            # alt_gr + ...
            # ---------------------------------------------------------------------
            # ---------------------------------------------------------------------
            # standalone keys
            # ---------------------------------------------------------------------
            # esc
            KeyCombo(
                mode=Mode(),
                key=Key(esc=True),
                legend=[
                    "Press ESC key.",
                ],
            ),
            # tab
            KeyCombo(
                mode=Mode(),
                key=Key(tab=True),
                legend=["Press TAB key."],
            ),
            # enter
            KeyCombo(
                mode=Mode(),
                key=Key(enter=True),
                legend=["Press ENTER key."],
            ),
            # del
            KeyCombo(
                mode=Mode(),
                key=Key(delete=True),
                legend=["Press DEL key."],
            ),
            # ---------------------------------------------------------------------
            # ctrl + ...
            # ---------------------------------------------------------------------
            # ctrl + a
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="a"),
                legend=[
                    "Select all.",
                ],
            ),
            # ctrl + b
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="b"),
                legend=[
                    "Boldify.",
                ],
            ),
            # ctrl + c
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="c"),
                legend=[
                    "Copy a selection to the clipboard.",
                ],
            ),
            # ctrl + f
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="f"),
                legend=[
                    "Chrome,etc: Start searching on the page.",
                ],
            ),
            # ctrl + g
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="g"),
                legend=[
                    "Chrome,etc: Find NEXT on the page.",
                ],
            ),
            # ctrl + i
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="i"),
                legend=[
                    "Italicize.",
                ],
            ),
            # ctrl + q
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="q"),
                legend=[
                    "Linux: Close the application.",
                ],
            ),
            # ctrl + s
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="s"),
                legend=[
                    "Save.",
                ],
            ),
            # ctrl + u
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="u"),
                legend=[
                    "Underline.",
                ],
            ),
            # ctrl + v
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="v"),
                legend=[
                    "Paste from the clipboard.",
                ],
            ),
            # ctrl + w
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="w"),
                legend=[
                    "Multitab: Close the current tab.",
                ],
            ),
            # ctrl + x
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="x"),
                legend=[
                    "Cut to clipboard.",
                ],
            ),
            # ctrl + y
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="y"),
                legend=[
                    "Re-do.",
                ],
            ),
            # ctrl + z
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="z"),
                legend=[
                    "Undo.",
                ],
            ),
            # ctrl + tab
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(tab=True),
                legend=[
                    "Multitab: Switch to the next tab. -->",
                ],
            ),
            # ---------------------------------------------------------------------
            # shift + ...
            # ---------------------------------------------------------------------
            # ---------------------------------------------------------------------
            # ctrl + shift + ...
            # ---------------------------------------------------------------------
            # ctrl + shift + tab
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(tab=True),
                legend=[
                    "Multitab: Switch to the previous tab. <--",
                ],
            ),
            # ctrl + shift + g
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="g"),
                legend=[
                    "Chrome,etc: Find PREVIOUS on the page.",
                ],
            ),
            # ---------------------------------------------------------------------
            # shift + alt + ...
            # ---------------------------------------------------------------------
            # shift + alt + tab
            KeyCombo(
                mode=Mode(shift=True, alt=True),
                key=Key(tab=True),
                legend=[
                    "Windows: Task swtcher backward. <--",
                ],
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
