"""
"""
from __future__ import annotations


class Mode:
    """
        Instance of `Mode` holds combination of modifier keys.

        Modifiers keys are alt, alt-gr, ctrl, ctrl-gr, shift.

    """

    def __init__(self,
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

    def __eq__(self, other: Mode) -> bool:
        return ((self.alt == other.alt)
                and (self.alt_gr == other.alt_gr)
                and (self.ctrl == other.ctrl)
                and (self.ctrl_gr == other.ctrl_gr)
                and (self.shift == other.shift)
                and (self.win == other.win)
                )

    def update(self, is_set: bool, name: str) -> None:

        if name in ("alt", "left alt", ):
            self.alt = is_set
        elif name in ("alt gr", "right alt", ):
            self.alt_gr = is_set
        elif name in ("ctrl", "left ctrl", ):
            self.ctrl = is_set
        elif name in ("right ctrl", ):
            # print(f"ctrl_gr = {is_set}")
            self.ctrl_gr = is_set
        elif name in ("shift", "right shift", "left shift", ):
            self.shift = is_set

    def is_expected(self, expected: Mode) -> bool:

        alt_eq = (self.alt == expected.alt)
        alt_gr = (self.alt_gr == expected.alt_gr)
        shift_eq = (self.shift == expected.shift)

        if expected.ctrl_gr:
            ctrl_eq = ((self.ctrl_gr == expected.ctrl_gr)
                       and not self.ctrl
                       and not expected.ctrl)
        else:
            ctrl_eq = ((self.ctrl or self.ctrl_gr) == (expected.ctrl or expected.ctrl_gr))

        return alt_eq and alt_gr and ctrl_eq and shift_eq
