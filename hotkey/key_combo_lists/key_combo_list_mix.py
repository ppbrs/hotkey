""" Configure the hotkeys that are related to various topics:
Chrome, vim, python.
"""
# pylint: disable=import-error

# Standard library imports
# Third party imports
from pybp.log import Log
# Local application imports
from hotkey.key_combo_lists.key_combo_list_interface import KeyComboListInterface
from hotkey.key_combo import Key_combo
from hotkey.mode import Mode
from hotkey.key import Key


class KeyComboListMix(KeyComboListInterface):
    """ Data class that holds specific hotkeys. """
    LEGEND_PREFIX = "MIX"

    def _get(self, log: Log) -> list[Key_combo]:
        return [

            # ---------------------------------------------------------------------
            # standalone keys
            # ---------------------------------------------------------------------
            # s
            Key_combo(mode=Mode(), key=Key(specific="s"),
                      legend=["Pinta: Cycle through \"Rectange\", \"Ellipse\", and \"Magic Wand\" select tools.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # tab
            Key_combo(mode=Mode(), key=Key(tab=True),
                      legend=["Chrome: Jump to the next control. -->", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),

            # ---------------------------------------------------------------------
            # alt + ...
            # ---------------------------------------------------------------------
            # alt + 1
            Key_combo(mode=Mode(alt=True), key=Key(specific="1"),
                      legend=["Nautilus: Show TAB #1.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # alt + 2
            Key_combo(mode=Mode(alt=True), key=Key(specific="2"),
                      legend=["Nautilus: Show TAB #2.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),

            # ---------------------------------------------------------------------
            # alt_gr + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # ctrl + ...
            # ---------------------------------------------------------------------
            # ctrl + [
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="["),
                      legend=["vim: Go to normal mode.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + d
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="d"),
                      legend=["Python interpreter: Exit.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + h
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="h"),
                      legend=["Nautilus: Toggle showing hidden files.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + k
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="k"),
                      legend=["Google Document: Add a link.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + l
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="l"),
                      legend=["Chrome: Focus on address bar.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + n
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="n"),
                      legend=[
                          "Chrome: Open new (normal, non-incognito) WINDOW.",
                          "Nautilus: Open a new Nautilus WINDOW pointing at the same directory."],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + o
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="o"),
                      legend=["Obsidian: Open a note.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + r
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="r"),
                      legend=["Pinta: Resize the image (= change resolution).", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + t
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="t"),
                      legend=["Chrome: Open a new TAB.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + enter
            Key_combo(mode=Mode(ctrl=True), key=Key(enter=True),
                      legend=[
                          "wandbox.org: Build and run.",
                          "Obsidian: Open the link under the cursor in a new tab.",
                          "Nautilus: Open a new Nautilus TAB looking inside the selected directory."],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + 1
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="1"),
                      legend=["Nautilus: Show files/directories as a list.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + 2
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="2"),
                      legend=["Nautilus: Show files/directories as a grid.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + /
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="/"),
                      legend=["Google Document: Open the list of hotkeys.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + [
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="["),
                      legend=["Obsidian: [CUSTOM] Show tags.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + ]
            Key_combo(mode=Mode(ctrl=True), key=Key(specific="]"),
                      legend=["Obsidian: [CUSTOM] Show outline.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),

            # ---------------------------------------------------------------------
            # shift + ...
            # ---------------------------------------------------------------------
            # shift + tab
            Key_combo(mode=Mode(shift=True), key=Key(tab=True),
                      legend=["Chrome: Jump to the previous control. <--", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # shift + enter
            Key_combo(mode=Mode(shift=True), key=Key(enter=True),
                      legend=[
                          "Telegram, Teams: Make a new line (without sending the message).",
                          "Nautilus: Open a new Nautilus WINDOW looking inside the selected directory."],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # shift + ` = ~
            Key_combo(mode=Mode(shift=True), key=Key(specific="`"),
                      legend=["Nautilus: Go to home directory (Press this and then enter.).", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),

            # ---------------------------------------------------------------------
            # ctrl + shift + ...
            # ---------------------------------------------------------------------
            # ctrl + shift + b
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="b"),
                      legend=[
                          "Chrome: Toggle the bookmarks bar.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + shift + f
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="f"),
                      legend=["Obsidian: Search.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + shift + n
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="n"),
                      legend=[
                          "Chrome: Open new incognito window.",
                          "Nautilus: Create a new directory."],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + shift + o
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="o"),
                      legend=["Chrome: Open the bookmarks manager.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + shift + r
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="r"),
                      legend=["Pinta: Resize the canvas (= expand the canvas).", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + shift + v
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="v"),
                      legend=["Obsidian: [CUSTOM]: Open a vault.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + shift + x
            Key_combo(mode=Mode(ctrl=True, shift=True), key=Key(specific="x"),
                      legend=["Pinta: Crop selection.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),

            # ---------------------------------------------------------------------
            # shift + alt + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # ctrl + alt + ...
            # ---------------------------------------------------------------------
            # ctrl + alt + c
            Key_combo(mode=Mode(ctrl=True, alt=True), key=Key(specific="c"),
                      legend=["Google Document: Copy formatting to clipboard.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + alt + v
            Key_combo(mode=Mode(ctrl=True, alt=True), key=Key(specific="v"),
                      legend=["Google Document: Paste formatting from clipboard.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + alt + x
            Key_combo(mode=Mode(ctrl=True, alt=True), key=Key(specific="x"),
                      legend=["Pinta: Auto crop.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + alt + 0
            Key_combo(mode=Mode(ctrl=True, alt=True), key=Key(specific="0"),
                      legend=["Google Document: Apply `Normal Text`.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + alt + 1
            Key_combo(mode=Mode(ctrl=True, alt=True), key=Key(specific="1"),
                      legend=["Google Document: Apply `Normal Heading 1`.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + alt + 2
            Key_combo(mode=Mode(ctrl=True, alt=True), key=Key(specific="2"),
                      legend=["Google Document: Apply `Normal Heading 2`.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),
            # ctrl + alt + 3
            Key_combo(mode=Mode(ctrl=True, alt=True), key=Key(specific="3"),
                      legend=["Google Document: Apply `Normal Heading 3`.", ],
                      weight=self.WEIGHT_NORMAL,
                      log=log
                      ),

            # ---------------------------------------------------------------------
            # ctrl-gr + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------
            # win + ...
            # ---------------------------------------------------------------------

            # ---------------------------------------------------------------------

        ]
