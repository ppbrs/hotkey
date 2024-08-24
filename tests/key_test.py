"""Tests for Key class."""

import unittest

from hotkey.key import Key


class KeyTest(unittest.TestCase):
    """Hold tests for Key class."""

    letters_list = [chr(c) for c in range(ord("a"), ord("z") + 1)]
    digits_list = [chr(c) for c in range(ord("0"), ord("9") + 1)]
    symbols_list = ["`", "-", "=", "[", "]", "\\", ";", '"', ",", ".", "/", "space"]
    count = 1000
    """Number of repetitions for each test."""

    def test_letters(self) -> None:
        """Test Key with `letters` parameter."""
        for _ in range(self.count):
            sut = Key(letters=True)
            self.assertTrue(sut.key in self.letters_list, "Key is not in valid range")

    def test_digits(self) -> None:
        """Test Key with `digits` parameter."""
        for _ in range(self.count):
            sut = Key(digits=True)
            self.assertTrue(sut.key in self.digits_list, "Key is not in valid range")

    def test_symbols(self) -> None:
        """Test Key with `symbols` parameter."""
        for _ in range(self.count):
            sut = Key(symbols=True)
            self.assertTrue(
                sut.key in self.symbols_list,
                f"Key `{sut.key}`is not in valid range: {self.symbols_list}",
            )

    def test_chars(self) -> None:
        """Test Key with `chars` parameter."""
        for _ in range(self.count):
            sut = Key(chars=True)
            self.assertTrue(
                sut.key in (self.letters_list + self.digits_list + self.symbols_list),
                "Key is not in valid range",
            )

    def test_esc(self) -> None:
        """Test Key with `esc` parameter."""
        for _ in range(self.count):
            sut = Key(esc=True)
            self.assertEqual(sut.key, "esc", "Key has wrong value")

    def test_backspace(self) -> None:
        """Test Key with `backspace` parameter."""
        for _ in range(self.count):
            sut = Key(backspace=True)
            self.assertEqual(sut.key, "backspace", "Key has wrong value")

    def test_enter(self) -> None:
        """Test Key with `enter` parameter."""
        for _ in range(self.count):
            sut = Key(enter=True)
            self.assertEqual(sut.key, "enter", "Key has wrong value")

    def test_tab(self) -> None:
        """Test Key with `tab` parameter."""
        for _ in range(self.count):
            sut = Key(tab=True)
            self.assertEqual(sut.key, "tab", "Key has wrong value")

    def test_nonchars(self) -> None:
        """Test Key with `nonchars` parameter."""
        for _ in range(self.count):
            sut = Key(nonchars=True)
            self.assertTrue(
                sut.key in ("esc", "delete", "backspace", "enter", "tab"),
                "Key is not in valid range",
            )

    def test_specific(self) -> None:
        """Test Key with specific parameters."""
        test_sets = [
            ("a", "a"),
            ("A", "a"),
            ("z", "z"),
            ("Z", "z"),
            ("`", "`"),
            ("~", "`"),
            ("1", "1"),
            ("!", "1"),
            ("2", "2"),
            ("@", "2"),
            ("3", "3"),
            ("#", "3"),
            ("4", "4"),
            ("$", "4"),
            ("5", "5"),
            ("%", "5"),
            ("6", "6"),
            ("^", "6"),
            ("7", "7"),
            ("&", "7"),
            ("8", "8"),
            ("*", "8"),
            ("9", "9"),
            ("(", "9"),
            ("0", "0"),
            (")", "0"),
            ("-", "-"),
            ("_", "-"),
            ("=", "="),
            ("+", "="),
        ]

        for test_set in test_sets:
            sut = Key(specific=test_set[0])
            self.assertTrue(
                (sut.key == test_set[1]),
                msg=f"Key `{sut.key}` has unexpected value, `{test_set[1]}` is expected",
            )

    def test_all_nonspecific(self) -> None:
        """Test Key with all non-specific parameters."""
        for _ in range(self.count):
            sut = Key(letters=True, digits=True, symbols=True, esc=True, backspace=True, enter=True)
            self.assertEqual(type(sut.key), str, "Wrong type")
            self.assertTrue(
                (
                    (sut.key in self.digits_list)
                    or (sut.key in self.letters_list)
                    or (sut.key in self.symbols_list)
                    or (sut.key == "esc")
                    or (sut.key == "backspace")
                    or (sut.key == "enter")
                ),
                "Key is not in valid range",
            )

    def test_none(self) -> None:
        """Test empty Key."""
        for _ in range(self.count):
            with self.assertRaises(ValueError):
                Key()

    def test_compare(self) -> None:
        """Test Key.__eq__()."""
        self.assertEqual(Key(esc=True), Key(esc=True), "`esc` must be equal to `esc`")
        self.assertEqual(Key(enter=True), Key(enter=True), "`enter` must be equal to `enter`")
        self.assertEqual(
            Key(backspace=True), Key(backspace=True), "`backspace` must be equal to `backspace`"
        )
        self.assertNotEqual(Key(esc=True), Key(backspace=True), "")
        self.assertNotEqual(Key(esc=True), Key(enter=True), "")
        self.assertNotEqual(Key(enter=True), Key(esc=True), "")
        self.assertNotEqual(Key(enter=True), Key(backspace=True), "")
        self.assertNotEqual(Key(backspace=True), Key(esc=True), "")
        self.assertNotEqual(Key(backspace=True), Key(enter=True), "")

        sut_1 = Key(symbols=True)
        sut_2 = Key(symbols=True)
        sut_1.key = "x"
        sut_2.key = "X"
        self.assertEqual(sut_1, sut_2, f"{str(sut_1)} must be equal to {str(sut_2)}")
        sut_1.key = "X"
        sut_2.key = "x"
        self.assertEqual(sut_1, sut_2, f"{str(sut_1)} must be equal to {str(sut_2)}")

    def test_repr(self) -> None:
        """Test Key.__repr__()."""
        self.assertEqual(str(Key(specific="l")), "L")


def main() -> None:
    """Standalone main, used for debugging."""
    unittest.main()


if __name__ == "__main__":
    main()
