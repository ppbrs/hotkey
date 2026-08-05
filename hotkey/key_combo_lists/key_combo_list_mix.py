"""Configure the hotkeys that are related to various topics:
Chrome, vim, python.
"""

from hotkey.key import Key
from hotkey.key_combo import KeyCombo
from hotkey.key_combo_lists.key_combo_list_interface import KeyComboListInterface
from hotkey.mode import Mode

from termcolor import colored

# "noqa" in class's first line silences the error that I cannot explain:
# Class cannot subclass "KeyComboListInterface" (has type "Any")  [misc] [mypy]


class KeyComboListMix(KeyComboListInterface):  # pylint: disable=too-few-public-methods # noqa
    """Data class that holds specific hotkeys."""

    LEGEND_PREFIX = "MIX"

    def _get(self) -> list[KeyCombo]:
        pinta = colored("PINTA", attrs=["bold"])
        chrome = colored("CHROME", attrs=["bold"])
        ubuntu = colored("UBUNTU", attrs=["bold"])
        google_sheets = colored("GOOGLE SHEETS", attrs=["bold"])
        return [
            # ---------------------------------------------------------------------
            # standalone keys
            # ---------------------------------------------------------------------
            # s
            KeyCombo(
                mode=Mode(),
                key=Key(specific="s"),
                legend=[
                    f'{pinta}: Cycle through "Rectange", "Ellipse", and "Magic Wand" select tools.',
                ],
            ),
            # tab
            KeyCombo(
                mode=Mode(),
                key=Key(tab=True),
                legend=[
                    f"{chrome}: Jump to the next control. -->",
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
                    "Google Document: Decrease indent.",
                ],
            ),
            # ctrl + ]
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="]"),
                legend=[
                    "Google Document: Increase indent.",
                ],
            ),
            # ctrl + 1
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="1"),
                legend=[
                    f"{chrome}: Switch to the 1st (leftmost) tab.",
                ],
            ),
            # ctrl + 2
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="2"),
                legend=[
                    f"{chrome}: Switch to the 2nd (from the left) tab.",
                ],
            ),
            # ctrl + d
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="d"),
                legend=[
                    "Python interpreter: Exit.",
                    "Google Meet: Mute/Unmute your microphone.",
                ],
            ),
            # ctrl + e
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="e"),
                legend=[
                    "Google Meet: Turn camera ON or OFF.",
                ],
            ),
            # ctrl + g
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="g"),
                legend=[
                    f"{pinta}: Rotate 90° counter-clockwise.",
                ],
            ),
            # ctrl + h
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="h"),
                legend=[
                    "Nautilus: Toggle showing hidden files.",
                    f"{pinta}: Rotate 90° clockwise.",
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
                    f"{chrome}: Focus on address bar.",
                ],
            ),
            # ctrl + n
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="n"),
                legend=[
                    f"{chrome}: Open new (normal, non-incognito) WINDOW.",
                    "Nautilus: Open a new Nautilus WINDOW pointing at the same directory.",
                ],
            ),
            # ctrl + r
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="r"),
                legend=[
                    f"{pinta}: Resize the image (= change resolution).",
                ],
            ),
            # ctrl + t
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="t"),
                legend=[
                    f"{chrome}: Open a new TAB.",
                ],
            ),
            # ctrl + enter
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(enter=True),
                legend=[
                    "godbolt.org: Recompile (When in manual recompile mode).",
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
                    f"{google_sheets}: Insert current DATE.",
                ],
            ),
            # ctrl + `
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="`"),
                legend=[
                    f"{google_sheets}: Toggle result and formula.",
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
                    f"{chrome}: Jump to the previous control. <--",
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
            # shift + h = H
            KeyCombo(
                mode=Mode(shift=True),
                key=Key(specific="h"),
                legend=[
                    f"{chrome}: Vimium: Go back in history.",
                ],
            ),
            # shift + l = L
            KeyCombo(
                mode=Mode(shift=True),
                key=Key(specific="L"),
                legend=[
                    f"{chrome}: Vimium: Go forward in history.",
                ],
            ),
            # ---------------------------------------------------------------------
            # ctrl + shift + ...
            # ---------------------------------------------------------------------
            # ctrl + shift + enter
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(enter=True),
                legend=[
                    "godbolt.org: Toggle between the manual and automatic recompile mode).",
                ],
            ),
            # ctrl + shift + b
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="b"),
                legend=[
                    f"{chrome}: Toggle the bookmarks bar.",
                ],
            ),
            # ctrl + shift + n
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="n"),
                legend=[f"{chrome}: Open new incognito window.", "Nautilus: Create a new directory."],
            ),
            # ctrl + shift + o
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="o"),
                legend=[
                    f"{chrome}: Open the bookmarks manager.",
                ],
            ),
            # ctrl + shift + r
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="r"),
                legend=[
                    f"{pinta}: Resize the canvas (= expand the canvas).",
                ],
            ),
            # ctrl + shift + u
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="u"),
                legend=[
                    f"{ubuntu}: Unicode symbol prefix.",
                ],
            ),
            # ctrl + shift + x
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="x"),
                legend=[
                    f"{pinta}: Crop selection.",
                ],
            ),
            # ctrl + shift + 7
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="7"),
                legend=[
                    "Google Document: Numbered list.",
                ],
            ),
            # ctrl + shift + 8
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="8"),
                legend=[
                    "Google Document: Bulleted list.",
                ],
            ),
            # ctrl + shift + 9
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="9"),
                legend=[
                    "Google Document: Check list.",
                ],
            ),
            # ctrl + shift + ;
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific=";"),
                legend=[
                    f"{google_sheets}: Insert current TIME.",
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
                    f"{pinta}: Auto crop.",
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
            # ctrl + alt + shift + ...
            # ---------------------------------------------------------------------
            # ctrl + alt + shift + ;
            KeyCombo(
                mode=Mode(ctrl=True, shift=True, alt=True),
                key=Key(specific=";"),
                legend=[
                    f"{google_sheets}: Insert current DATE and TIME.",
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
