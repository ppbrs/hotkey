"""Configure the hotkeys that are specific to sublime-text."""

from hotkey.key import Key
from hotkey.key_combo import KeyCombo
from hotkey.key_combo_lists.key_combo_list_interface import KeyComboListInterface
from hotkey.mode import Mode

# "noqa" in class's first line silences the error that I cannot explain:
# Class cannot subclass "KeyComboListInterface" (has type "Any")  [misc] [mypy]


class KeyComboListVscode(KeyComboListInterface):  # pylint: disable=too-few-public-methods  # noqa
    """Data class that holds specific hotkeys."""

    LEGEND_PREFIX = "VS CODE"

    def _get(self) -> list[KeyCombo]:
        return [
            # ---------------------------------------------------------------------
            # alt + ...
            # ---------------------------------------------------------------------
            # alt + [
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="["),
                legend=[
                    "CUSTOM: Select PREVIOUS suggestion.",
                ],
            ),
            # alt + ]
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="]"),
                legend=[
                    "CUSTOM: Select NEXT suggestion.",
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
            # ctrl + space
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="space"),
                legend=[
                    "Toggle suggestions and suggestion details.",
                ],
            ),
            # ctrl + `
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="`"),
                legend=[
                    "Toggle the integrated Terminal.",
                ],
            ),
            # ctrl + B
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="b"),
                legend=[
                    "Toggle the sidebar.",
                ],
            ),
            # ctrl + T
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="t"),
                legend=[
                    "Select a symbol. Project-scope.",
                ],
            ),
            # ---------------------------------------------------------------------
            # shift + ...
            # ---------------------------------------------------------------------
            # ---------------------------------------------------------------------
            # ctrl + shift + ...
            # ---------------------------------------------------------------------
            # ctrl + shift + d
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="d"),
                legend=[
                    'Open "Debug" view.',
                ],
            ),
            # ctrl + shift + e
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="e"),
                legend=[
                    'Open "Explore" view.',
                ],
            ),
            # ctrl + shift + i
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="i"),
                legend=[
                    "Format the file (ruff, rustfmt, ...)",
                ],
            ),
            # ctrl + shift + L
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="L"),
                legend=[
                    "Select all occurences of the selected word",
                ],
            ),
            # ctrl + shift + M
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="M"),
                legend=[
                    'Toggle "Problems" panel',
                ],
            ),
            # ctrl + shift + O
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="o"),
                legend=[
                    "Select a symbol. File-scope.",
                ],
            ),
            # ctrl + shift + y
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="y"),
                legend=[
                    'Toggle "Debug Console" panel.',
                ],
            ),
            # ctrl + shift + \
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="\\"),
                legend=[
                    "Jump to the matching bracket.",
                ],
            ),
            # ctrl + shift + ;
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific=";"),
                legend=[
                    "Focus on breadcrumbs.",
                ],
            ),
            # ctrl + shift + .
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="."),
                legend=[
                    "Focus on breadcrumbs. Dropdown select.",
                ],
            ),
            # ---------------------------------------------------------------------
            # shift + alt + ...
            # ---------------------------------------------------------------------
            # shift + alt + tab
            # ---------------------------------------------------------------------
            # ctrl + alt + ...
            # ---------------------------------------------------------------------
            # ctrl + alt + s
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="s"),
                legend=[
                    "Source Control: Stage selected range. (After Ctrl-K)",
                ],
            ),
            # ---------------------------------------------------------------------
            # ctrl-gr + ...
            # ---------------------------------------------------------------------
            # ---------------------------------------------------------------------
            # win + ...
            # ---------------------------------------------------------------------
        ]
