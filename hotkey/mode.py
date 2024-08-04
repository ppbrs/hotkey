"""Mode class."""
from __future__ import annotations

ModifierKey = str
"""
Distinct modifiers keys are:
    "alt",
    "alt-gr",
    "ctrl",
    "ctrl-gr",
    "shift",
    "win".
"""


class Mode:
    """Instance of `Mode` holds combination of modifier keys."""

    modifier_keys = [
        "alt", "left alt",
        "alt gr", "right alt",
        "ctrl", "right ctrl", "left ctrl",
        "shift", "right shift", "left shift",
        "left windows",
    ]

    def __init__(  # pylint: disable=too-many-arguments
        self,
        ctrl: bool = False,
        ctrl_gr: bool = False,
        alt: bool = False,
        alt_gr: bool = False,
        shift: bool = False,
        win: bool = False
    ) -> None:

        if alt and alt_gr:
            raise ValueError("Mode with `alt` and `alt-gr` is not possible")
        if ctrl and ctrl_gr:
            raise ValueError("Mode with `ctrl` and `ctrl-gr` is not possible")

        self.alt = alt
        self.alt_gr = alt_gr
        self.ctrl = ctrl
        self.ctrl_gr = ctrl_gr
        self.shift = shift
        self.win = win

    def __repr__(self) -> str:

        modifiers_list = []
        if self.ctrl:
            modifiers_list.append("ctrl")
        if self.ctrl_gr:
            modifiers_list.append("ctrl-gr")
        if self.alt:
            modifiers_list.append("alt")
        if self.alt_gr:
            modifiers_list.append("alt-gr")
        if self.shift:
            modifiers_list.append("shift")
        if self.win:
            modifiers_list.append("win")
        return " + ".join(modifiers_list)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Mode):
            return False
        alt_eq = self.alt == other.alt
        alt_gr_eq = self.alt_gr == other.alt_gr
        shift_eq = self.shift == other.shift

        if other.ctrl_gr:
            ctrl_eq = ((self.ctrl_gr == other.ctrl_gr)
                       and not self.ctrl
                       and not other.ctrl)
        else:
            ctrl_eq = (self.ctrl or self.ctrl_gr) == (other.ctrl or other.ctrl_gr)
        win_eq = self.win == other.win

        return alt_eq and alt_gr_eq and ctrl_eq and shift_eq and win_eq

    def update(self, is_set: bool, modifier_key: ModifierKey) -> None:
        """Add to or remove the modifier from the mode.
        """
        if modifier_key in ("alt", "left alt", ):
            self.alt = is_set
        elif modifier_key in ("alt gr", "right alt", ):
            self.alt_gr = is_set
        elif modifier_key in ("ctrl", "left ctrl", ):
            self.ctrl = is_set
        elif modifier_key in ("right ctrl", ):
            # print(f"ctrl_gr = {is_set}")
            self.ctrl_gr = is_set
        elif modifier_key in ("shift", "right shift", "left shift", ):
            self.shift = is_set
