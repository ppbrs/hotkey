"""Configure the hotkeys that are related to various topics:
Chrome, vim, python.
"""

from hotkey.key import Key
from hotkey.key_combo import KeyCombo
from hotkey.key_combo_lists.key_combo_list_interface import KeyComboListInterface
from hotkey.mode import Mode

# "noqa" in class's first line silences the error that I cannot explain:
# Class cannot subclass "KeyComboListInterface" (has type "Any")  [misc] [mypy]

class KeyComboListMix(KeyComboListInterface):  # pylint: disable=too-few-public-methods # noqa
    """Data class that holds specific hotkeys."""

    LEGEND_PREFIX = "MIX"

    def _get(self) -> list[KeyCombo]:
        return [
            # ---------------------------------------------------------------------
            # standalone keys
            # ---------------------------------------------------------------------
            # s
            KeyCombo(
                mode=Mode(),
                key=Key(specific="s"),
                legend=[
                    'Pinta: Cycle through "Rectange", "Ellipse", and "Magic Wand" select tools.',
                ],
            ),
            # tab
            KeyCombo(
                mode=Mode(),
                key=Key(tab=True),
                legend=[
                    "Chrome: Jump to the next control. -->",
                ],
            ),
            # ---------------------------------------------------------------------
            # alt + ...
            # ---------------------------------------------------------------------
            # alt + 1
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="1"),
                legend=[
                    "Nautilus: Show TAB #1.",
                ],
            ),
            # alt + 2
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="2"),
                legend=[
                    "Nautilus: Show TAB #2.",
                ],
            ),
            # ---------------------------------------------------------------------
            # alt_gr + ...
            # ---------------------------------------------------------------------
            # ---------------------------------------------------------------------
            # ctrl + ...
            # ---------------------------------------------------------------------
            # ctrl + [
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="["),
                legend=[
                    "vim: Go to normal mode.",
                ],
            ),
            # ctrl + d
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="d"),
                legend=[
                    "Python interpreter: Exit.",
                ],
            ),
            # ctrl + h
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="h"),
                legend=[
                    "Nautilus: Toggle showing hidden files.",
                ],
            ),
            # ctrl + k
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="k"),
                legend=[
                    "Google Document: Add a link.",
                ],
            ),
            # ctrl + l
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="l"),
                legend=[
                    "Chrome: Focus on address bar.",
                ],
            ),
            # ctrl + n
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="n"),
                legend=[
                    "Chrome: Open new (normal, non-incognito) WINDOW.",
                    "Nautilus: Open a new Nautilus WINDOW pointing at the same directory.",
                ],
            ),
            # ctrl + r
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="r"),
                legend=[
                    "Pinta: Resize the image (= change resolution).",
                ],
            ),
            # ctrl + t
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="t"),
                legend=[
                    "Chrome: Open a new TAB.",
                ],
            ),
            # ctrl + enter
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(enter=True),
                legend=[
                    "wandbox.org: Build and run.",
                    "Nautilus: Open a new Nautilus TAB looking inside the selected directory.",
                ],
            ),
            # ctrl + 1
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="1"),
                legend=[
                    "Nautilus: Show files/directories as a list.",
                ],
            ),
            # ctrl + 2
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="2"),
                legend=[
                    "Nautilus: Show files/directories as a grid.",
                ],
            ),
            # ctrl + /
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="/"),
                legend=[
                    "Google Document: Open the list of hotkeys.",
                ],
            ),
            # ctrl + ;
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific=";"),
                legend=[
                    "Google Sheets: Insert current date.",
                ],
            ),
            # ---------------------------------------------------------------------
            # shift + ...
            # ---------------------------------------------------------------------
            # shift + tab
            KeyCombo(
                mode=Mode(shift=True),
                key=Key(tab=True),
                legend=[
                    "Chrome: Jump to the previous control. <--",
                ],
            ),
            # shift + enter
            KeyCombo(
                mode=Mode(shift=True),
                key=Key(enter=True),
                legend=[
                    "Telegram, Teams: Make a new line (without sending the message).",
                    "Nautilus: Open a new Nautilus WINDOW looking inside the selected directory.",
                ],
            ),
            # shift + ` = ~
            KeyCombo(
                mode=Mode(shift=True),
                key=Key(specific="`"),
                legend=[
                    "Nautilus: Go to home directory (Press this and then enter.).",
                ],
            ),
            # ---------------------------------------------------------------------
            # ctrl + shift + ...
            # ---------------------------------------------------------------------
            # ctrl + shift + b
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="b"),
                legend=[
                    "Chrome: Toggle the bookmarks bar.",
                ],
            ),
            # ctrl + shift + n
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="n"),
                legend=["Chrome: Open new incognito window.", "Nautilus: Create a new directory."],
            ),
            # ctrl + shift + o
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="o"),
                legend=[
                    "Chrome: Open the bookmarks manager.",
                ],
            ),
            # ctrl + shift + r
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="r"),
                legend=[
                    "Pinta: Resize the canvas (= expand the canvas).",
                ],
            ),
            # ctrl + shift + x
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="x"),
                legend=[
                    "Pinta: Crop selection.",
                ],
            ),
            # ---------------------------------------------------------------------
            # shift + alt + ...
            # ---------------------------------------------------------------------
            # ---------------------------------------------------------------------
            # ctrl + alt + ...
            # ---------------------------------------------------------------------
            # ctrl + alt + c
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="c"),
                legend=[
                    "Google Document: Copy formatting to clipboard.",
                ],
            ),
            # ctrl + alt + v
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="v"),
                legend=[
                    "Google Document: Paste formatting from clipboard.",
                ],
            ),
            # ctrl + alt + x
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="x"),
                legend=[
                    "Pinta: Auto crop.",
                ],
            ),
            # ctrl + alt + 0
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="0"),
                legend=[
                    "Google Document: Apply `Normal Text`.",
                ],
            ),
            # ctrl + alt + 1
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="1"),
                legend=[
                    "Google Document: Apply `Normal Heading 1`.",
                ],
            ),
            # ctrl + alt + 2
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="2"),
                legend=[
                    "Google Document: Apply `Normal Heading 2`.",
                ],
            ),
            # ctrl + alt + 3
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="3"),
                legend=[
                    "Google Document: Apply `Normal Heading 3`.",
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
