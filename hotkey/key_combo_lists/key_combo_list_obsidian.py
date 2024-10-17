"""Configure the hotkeys that are related to Obsidian application."""

from hotkey.key import Key
from hotkey.key_combo import KeyCombo
from hotkey.key_combo_lists.key_combo_list_interface import KeyComboListInterface
from hotkey.mode import Mode

# "noqa" in class's first line silences the error that I cannot explain:
# Class cannot subclass "KeyComboListInterface" (has type "Any")  [misc] [mypy]

class KeyComboListObsidian(KeyComboListInterface):  # pylint: disable=too-few-public-methods # noqa
    """Data class that holds specific hotkeys."""

    LEGEND_PREFIX = "OBSIDIAN"

    def _get(self) -> list[KeyCombo]:
        return [
            # ---------------------------------------------------------------------
            # alt + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # alt_gr + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # standalone keys
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # ctrl + ...
            # ---------------------------------------------------------------------
            # ctrl + k
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="k"),
                legend=[
                    "CUSTOM: Add an internal link.",
                ],
            ),
            # ctrl + o
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="o"),
                legend=[
                    "Open a note.",
                ],
            ),
            # ctrl + [
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="["),
                legend=[
                    "CUSTOM Show tags.",
                ],
            ),
            # ctrl + ]
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="]"),
                legend=[
                    "CUSTOM Show outline.",
                ],
            ),
            # ctrl + enter
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(enter=True),
                legend=[
                    "Open the link under the cursor in a new tab.",
                ],
            ),

            # ---------------------------------------------------------------------
            # shift + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # ctrl + shift + ...
            # ---------------------------------------------------------------------
            # ctrl + shift + f
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="f"),
                legend=[
                    "Search.",
                ],
            ),
            # ctrl + shift + v
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="v"),
                legend=[
                    "CUSTOM: Open a vault.",
                ],
            ),

            # ---------------------------------------------------------------------
            # shift + alt + ...
            # ---------------------------------------------------------------------
            # shift + alt + D
            KeyCombo(
                mode=Mode(alt=True, shift=True),
                key=Key(specific="d"),
                legend=[
                    "CUSTOM: Switch to dark mode",
                ],
            ),
            # shift + alt + L
            KeyCombo(
                mode=Mode(alt=True, shift=True),
                key=Key(specific="l"),
                legend=[
                    "CUSTOM: Switch to ligth mode",
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
