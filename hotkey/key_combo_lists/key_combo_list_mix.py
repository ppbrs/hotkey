"""Configure the hotkeys that are related to various topics:
Chrome, vim, python.
"""

from hotkey.key import Key
from hotkey.key_combo import KeyCombo
from hotkey.key_combo_lists.key_combo_list_interface import KeyComboListInterface
from hotkey.mode import Mode


class KeyComboListMix(KeyComboListInterface):
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
                weight=self.WEIGHT_NORMAL,
            ),
            # tab
            KeyCombo(
                mode=Mode(),
                key=Key(tab=True),
                legend=[
                    "Chrome: Jump to the next control. -->",
                ],
                weight=self.WEIGHT_NORMAL,
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
                weight=self.WEIGHT_NORMAL,
            ),
            # alt + 2
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="2"),
                legend=[
                    "Nautilus: Show TAB #2.",
                ],
                weight=self.WEIGHT_NORMAL,
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
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + d
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="d"),
                legend=[
                    "Python interpreter: Exit.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + h
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="h"),
                legend=[
                    "Nautilus: Toggle showing hidden files.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + k
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="k"),
                legend=[
                    "Google Document: Add a link.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + l
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="l"),
                legend=[
                    "Chrome: Focus on address bar.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + n
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="n"),
                legend=[
                    "Chrome: Open new (normal, non-incognito) WINDOW.",
                    "Nautilus: Open a new Nautilus WINDOW pointing at the same directory.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + o
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="o"),
                legend=[
                    "Obsidian: Open a note.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + r
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="r"),
                legend=[
                    "Pinta: Resize the image (= change resolution).",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + t
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="t"),
                legend=[
                    "Chrome: Open a new TAB.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + enter
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(enter=True),
                legend=[
                    "wandbox.org: Build and run.",
                    "Obsidian: Open the link under the cursor in a new tab.",
                    "Nautilus: Open a new Nautilus TAB looking inside the selected directory.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + 1
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="1"),
                legend=[
                    "Nautilus: Show files/directories as a list.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + 2
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="2"),
                legend=[
                    "Nautilus: Show files/directories as a grid.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + /
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="/"),
                legend=[
                    "Google Document: Open the list of hotkeys.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + [
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="["),
                legend=[
                    "Obsidian: [CUSTOM] Show tags.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + ]
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="]"),
                legend=[
                    "Obsidian: [CUSTOM] Show outline.",
                ],
                weight=self.WEIGHT_NORMAL,
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
                weight=self.WEIGHT_NORMAL,
            ),
            # shift + enter
            KeyCombo(
                mode=Mode(shift=True),
                key=Key(enter=True),
                legend=[
                    "Telegram, Teams: Make a new line (without sending the message).",
                    "Nautilus: Open a new Nautilus WINDOW looking inside the selected directory.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # shift + ` = ~
            KeyCombo(
                mode=Mode(shift=True),
                key=Key(specific="`"),
                legend=[
                    "Nautilus: Go to home directory (Press this and then enter.).",
                ],
                weight=self.WEIGHT_NORMAL,
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
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + shift + f
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="f"),
                legend=[
                    "Obsidian: Search.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + shift + n
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="n"),
                legend=["Chrome: Open new incognito window.", "Nautilus: Create a new directory."],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + shift + o
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="o"),
                legend=[
                    "Chrome: Open the bookmarks manager.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + shift + r
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="r"),
                legend=[
                    "Pinta: Resize the canvas (= expand the canvas).",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + shift + v
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="v"),
                legend=[
                    "Obsidian: [CUSTOM]: Open a vault.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + shift + x
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="x"),
                legend=[
                    "Pinta: Crop selection.",
                ],
                weight=self.WEIGHT_NORMAL,
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
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + alt + v
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="v"),
                legend=[
                    "Google Document: Paste formatting from clipboard.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + alt + x
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="x"),
                legend=[
                    "Pinta: Auto crop.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + alt + 0
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="0"),
                legend=[
                    "Google Document: Apply `Normal Text`.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + alt + 1
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="1"),
                legend=[
                    "Google Document: Apply `Normal Heading 1`.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + alt + 2
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="2"),
                legend=[
                    "Google Document: Apply `Normal Heading 2`.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + alt + 3
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="3"),
                legend=[
                    "Google Document: Apply `Normal Heading 3`.",
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
