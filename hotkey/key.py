"""Key class."""
from __future__ import annotations

import random
from typing import Any


class Key:
    """
    An abstraction representing a key of a keyboard that is chosen randomly from all keys
    in a subset.
    """
    letters_list = [chr(c) for c in range(ord("a"), ord("z") + 1)]
    digits_list = [chr(c) for c in range(ord("0"), ord("9") + 1)]
    symbols_list = ["`", "-", "=", "[", "]", "\\", ";", "\"", ",", ".", "/", "space"]
    symbol_key_mapping = {
        "~": "`",
        "!": "1",
        "@": "2",
        "#": "3",
        "$": "4",
        "%": "5",
        "^": "6",
        "&": "7",
        "*": "8",
        "(": "9",
        ")": "0",
        "_": "-",
        "+": "=",
        "?": "/",
    }

    def __init__(
        self,
        letters: bool = False, digits: bool = False, symbols: bool = False,
        chars: bool = False, nonchars: bool = False,
        esc: bool = False, backspace: bool = False, enter: bool = False, tab: bool = False,
        delete: bool = False,
        specific: str | None = None
    ) -> None:
        """Chooses one key randomly according to the arguments.

        :param letters: key may be  chosen from letters from 'a' to 'z'.
        :param digits: key may be  chosen from digits from '0' to '9'
        :param symbols: key may be  chosen from any chars
            available on the keyboard except letters and digits.
        :param esc: Escape-key may be chosen.
        :param backspace: Backspace-key may be chosen.
        :param enter: Enter-key may be chosen.
        :param tab: Tab-key may be chosen.
        :param delete: Delete-key may be chosen.
        :param chars: Any letter or digit or symbol may be chosen.
        :param nonchars: Esc, enter, backspace, tab, or delete may by chosen.
        :param specific: Specific key

        :raises ValueError: when no argument is provided.
        """
        # pylint: disable=too-many-arguments

        variants = []
        if letters or chars:
            variants += self.letters_list
        if symbols or chars:
            variants += self.symbols_list
        if digits or chars:
            variants += self.digits_list

        if esc or nonchars:
            variants.append("esc")
        if backspace or nonchars:
            variants.append("backspace")
        if enter or nonchars:
            variants.append("enter")
        if delete or nonchars:
            variants.append("delete")
        if tab or nonchars:
            variants.append("tab")

        if specific is not None:
            # Check that the key is valid.
            if specific in self.symbol_key_mapping:
                specific = self.symbol_key_mapping[specific]
            elif specific.isupper():
                specific = specific.lower()
            variants.append(specific)

        if len(variants) == 0:
            raise ValueError("Error in parameters.")
        self.key = random.choice(variants)

    def __eq__(self, other: Any) -> bool:
        assert isinstance(other, Key)
        return (
            self.key == other.key
            or self.key.lower() == other.key
            or self.key == other.key.lower())

    def __repr__(self) -> str:
        ret_val = str(self.key)
        # Substitute keys that look ambiguous.
        if self.key == "l":  # `l` can be confused with `1`
            ret_val = "L"
        return ret_val


if __name__ == "__main__":
    pass
