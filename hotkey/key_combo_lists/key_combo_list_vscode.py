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
            # ---------------------------------------------------------------------
            # alt_gr + ...
            # ---------------------------------------------------------------------
            # ---------------------------------------------------------------------
            # standalone keys
            # ---------------------------------------------------------------------
            # ---------------------------------------------------------------------
            # ctrl + ...
            # ---------------------------------------------------------------------
            # ctrl + `
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="`"),
                legend=[
                    "Toggle the integrated Terminal.",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + b
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="b"),
                legend=[
                    "Toggle the sidebar.",
                ],
                weight=self.WEIGHT_NORMAL,
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
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + shift + e
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="e"),
                legend=[
                    'Open "Explore" view.',
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + shift + o
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="o"),
                legend=[
                    "Go to symbol ...",
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + shift + y
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="y"),
                legend=[
                    'Toggle "Debug Console".',
                ],
                weight=self.WEIGHT_NORMAL,
            ),
            # ctrl + shift + \ (generates SIGQUIT)
            # KeyCombo(
            #     mode=Mode(ctrl=True, shift=True),
            #     key=Key(specific="\\"),
            #     legend=[
            #         'Jump to a matching bracket.',
            #     ],
            #     weight=self.WEIGHT_NORMAL,
            # ),
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
