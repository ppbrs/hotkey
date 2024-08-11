"""Tests for Mode class."""
import unittest

from hotkey.mode import Mode


class ModeTest(unittest.TestCase):
    """Hold tests for Mode class."""

    def test_specific(self) -> None:
        """Test Mode with specific parameters."""

        sut = Mode(alt=False, alt_gr=False, ctrl=False, ctrl_gr=False, shift=False, win=False)
        self.assertEqual(str(sut), "", "Error in string representation")

        sut = Mode(alt=True, alt_gr=False, ctrl=False, ctrl_gr=False, shift=False, win=False)
        self.assertEqual(str(sut), "alt", "Error in string representation")

        sut = Mode(alt=False, alt_gr=True, ctrl=False, ctrl_gr=False, shift=False, win=False)
        self.assertEqual(str(sut), "alt-gr", "Error in string representation")

        sut = Mode(alt=False, alt_gr=False, ctrl=True, ctrl_gr=False, shift=False, win=False)
        self.assertEqual(str(sut), "ctrl", "Error in string representation")

        sut = Mode(alt=False, alt_gr=False, ctrl=False, ctrl_gr=True, shift=False, win=False)
        self.assertEqual(str(sut), "ctrl-gr", "Error in string representation")

        sut = Mode(alt=False, alt_gr=False, ctrl=False, ctrl_gr=False, shift=True, win=False)
        self.assertEqual(str(sut), "shift", "Error in string representation")

        sut = Mode(alt=False, alt_gr=False, ctrl=False, ctrl_gr=False, shift=False, win=True)
        self.assertEqual(str(sut), "win", "Error in string representation")

        sut = Mode(alt=True, alt_gr=False, ctrl=True, ctrl_gr=False, shift=False, win=False)
        self.assertEqual(str(sut), "ctrl + alt", "Error in string representation")

        sut = Mode(alt=True, alt_gr=False, ctrl=False, ctrl_gr=False, shift=True, win=False)
        self.assertEqual(str(sut), "alt + shift", "Error in string representation")

        sut = Mode(alt=False, alt_gr=False, ctrl=True, ctrl_gr=False, shift=True, win=False)
        self.assertEqual(str(sut), "ctrl + shift", "Error in string representation")

    def test_eq(self) -> None:
        """Test Mode.__eq__()."""
        # List of tuples. Each tuple:
        # 1. expected mode
        # 2. list of matching modes
        # 3. list of not matching modes
        test_sets: list[tuple[Mode, list[Mode], list[Mode]]] = [
            (Mode(alt=True),
             [Mode(alt=True), ],
             [Mode(), Mode(alt_gr=True), Mode(ctrl=True), Mode(ctrl_gr=True), Mode(shift=True), ],
             ),
            (Mode(alt_gr=True),
             [Mode(alt_gr=True), ],
             [Mode(), Mode(alt=True), Mode(ctrl=True), Mode(ctrl_gr=True), Mode(shift=True), ],
             ),
            (Mode(ctrl=True),
             [Mode(ctrl=True), Mode(ctrl_gr=True), ],
             [Mode(), Mode(alt=True), Mode(alt_gr=True), Mode(shift=True), ],
             ),
            (Mode(ctrl_gr=True),
             [Mode(ctrl_gr=True), ],
             [Mode(), Mode(alt=True), Mode(alt_gr=True), Mode(ctrl=True), Mode(shift=True), ],
             ),
            (Mode(shift=True),
             [Mode(shift=True), ],
             [Mode(), Mode(alt=True), Mode(alt_gr=True), Mode(ctrl=True), Mode(ctrl_gr=True), ],
             ),
        ]

        for test_set in test_sets:
            mode_expected = test_set[0]
            modes_matching = test_set[1]
            modes_nonmatching = test_set[2]
            for mode_matching in modes_matching:
                self.assertTrue(
                    mode_matching == mode_expected,
                    f"Pressed `{mode_matching}` must match expected `{mode_expected}`")
            for mode_nonmatching in modes_nonmatching:
                self.assertFalse(
                    mode_nonmatching == mode_expected,
                    f"Pressed `{mode_nonmatching}` should not match expected `{mode_expected}`")


def main() -> None:
    """Standalone main, used for debugging."""
    unittest.main()


if __name__ == "__main__":
    main()
