"""Configure the hotkeys that are specific to Visual Studio Code editor."""

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
                    "FIND and SEARCH: Match Case: Aa",
                ],
            ),
            # alt + q
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="q"),
                legend=[
                    "CUSTOM: Duplicate the line or selection",
                ],
            ),
            # alt + r
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="r"),
                legend=[
                    "FIND and SEARCH: Use Regular Expression: .*",
                ],
            ),
            # alt + w
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="w"),
                legend=[
                    "FIND and SEARCH: Use Whole Word: [ab]",
                ],
            ),
            # alt + z
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(specific="z"),
                legend=[
                    "Word Wrap.",
                ],
            ),
            # alt + enter
            KeyCombo(
                mode=Mode(alt=True),
                key=Key(enter=True),
                legend=["FIND: Select all."],
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
                    "SUGGEST: Choose the highlighted variant.",
                ],
            ),
            # ---------------------------------------------------------------------
            # ctrl + ...
            # ---------------------------------------------------------------------
            # ctrl + space
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="space"),
                legend=[
                    "SUGGEST: Trigger.",
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
            # ctrl + /
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="/"),
                legend=[
                    "Comment/Uncomment current line.",
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
            # ctrl + B
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="b"),
                legend=[
                    "Toggle the sidebar.",
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
            # ctrl + p
            KeyCombo(
                mode=Mode(ctrl=True),
                key=Key(specific="p"),
                legend=[
                    "Go to file ...",
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
            # shift + enter
            KeyCombo(
                mode=Mode(shift=True),
                key=Key(enter=True),
                legend=["FIND: Previous Match."],
            ),
            # ---------------------------------------------------------------------
            # ctrl + shift + ...
            # ---------------------------------------------------------------------
            # ctrl + shift + b
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="b"),
                legend=[
                    "Select a build task to run",
                ],
            ),
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
            # ctrl + shift + k
            KeyCombo(
                mode=Mode(ctrl=True, shift=True),
                key=Key(specific="k"),
                legend=[
                    "Delete the line.",
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
            # ctrl + shift + alt + \
            KeyCombo(
                mode=Mode(ctrl=True, shift=True, alt=True),
                key=Key(specific="\\"),
                legend=[
                    "CUSTOM: Select everything inside the brackets, braces,parentheses.",
                ],
            ),
            # ---------------------------------------------------------------------
            # shift + alt + ...
            # ---------------------------------------------------------------------
            # shift + alt + tab
            # ---------------------------------------------------------------------
            # ctrl + alt + ...
            # ---------------------------------------------------------------------
            # ctrl + alt + c
            # KeyCombo(
            #     mode=Mode(ctrl=True, alt=True),
            #     key=Key(specific="c"),
            #     legend=[
            #         "Copy file path",
            #     ],
            # ),
            # ctrl + alt + i
            KeyCombo(
                mode=Mode(ctrl=True, alt=True),
                key=Key(specific="i"),
                legend=[
                    "Toggle the CHAT.",
                ],
            ),
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
