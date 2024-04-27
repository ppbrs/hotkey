""" Key abstraction.
"""
from __future__ import annotations

import random

from hotkey.error import Error


class Key:
    """ An abstraction representing a key of a keyboard that is chosen randomly from all keys
    of a subset.

    Note: This class can be simplified because all keys created by the application are now specific.
    """

    class KeyError(Error):
        """ An exception thrown when a Key instance cannot be created.
        """

    letters_list = [chr(c) for c in range(ord("a"), ord("z") + 1)]
    digits_list = [chr(c) for c in range(ord("0"), ord("9") + 1)]
    symbols_list = ("`", "-", "=",
                    "[", "]", "\\",
                    ";", "\"",
                    ",", ".", "/",
                    "space")

    def __init__(self,
                 letters: bool = False, digits: bool = False, symbols: bool = False,
                 chars: bool = False, nonchars: bool = False,
                 esc: bool = False, backspace: bool = False, enter: bool = False, tab: bool = False,
                 delete: bool = False,
                 specific: str | None = None) -> None:
        """Chooses one key randomly according to the arguments.

        Args:
            letters: key may be  chosen from letters from 'a' to 'z'.
            digits: key may be  chosen from digits from '0' to '9'
            symbols: key may be  chosen from any chars
                available on the keyboard except letters and digits.
            esc: Escape-key may be chosen.
            backspace: Backspace-key may be chosen.
            enter: Enter-key may be chosen.
            tab: Tab-key may be chosen.
            delete: Delete-key may be chosen.
            chars: Any letter or digit or symbol may be chosen.
            nonchars: Esc, enter, backspace, tab, or delete may by chosen.
            specific: Specific key

        Returns:

        Raises:
            KeyError: when no argument is provided.

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
            dict_upper = {
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
            if specific in dict_upper:
                specific = dict_upper[specific]
            elif specific.isupper():
                specific = specific.lower()
            variants.append(specific)

        if len(variants) == 0:
            raise self.KeyError("Error in parameters.")

        self.key = random.choice(variants)

    def __eq__(self, other: Key) -> bool:  # type: ignore[override]
        assert isinstance(other, Key)
        return (self.key == other.key) or (self.key.lower() == other.key) \
            or (self.key == other.key.lower())

    def __repr__(self) -> str:
        ret_val = str(self.key)
        # Substitute keys that look ambiguous.
        if self.key == "l":  # `l` can be confused with `1`
            ret_val = "L"
        return ret_val


if __name__ == "__main__":
    pass
