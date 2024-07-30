"""KeyComboTest class."""
import threading
import time
import unittest
from collections.abc import Iterable

import keyboard  # type: ignore

from hotkey.key import Key
from hotkey.key_combo import KeyCombo
from hotkey.mode import Mode

from .event_fake import EventFake


class KeyComboTest(unittest.TestCase):
    """Test class for KeyCombo."""

    def _send_events(
        self,
        key_combo: KeyCombo,
        event_list: Iterable[EventFake],
    ) -> None:
        """Call KeyCombo callbacks with the events from the provided list."""
        time.sleep(0.1)
        for event in event_list:
            key_combo.callback(event)

    def test_alt_key_ok(self) -> None:
        """Test that KeyCombo captures events with alt key pressed."""

        test_sets = (
            # -----------------------------------------------------------------
            # Without modifiers:
            # -----------------------------------------------------------------
            {
                "mode": Mode(),
                "key.key": "a",
                "events":
                [
                    EventFake(event_type=keyboard.KEY_DOWN, name="a"),
                ],
                "result": True
            },
            {
                "mode": Mode(),
                "key.key": "a",
                "events": [
                    EventFake(event_type=keyboard.KEY_DOWN, name="b"),
                ],
                "result": False
            },
            # -----------------------------------------------------------------
            # alt + smth
            # -----------------------------------------------------------------
            {
                "mode": Mode(alt=True),
                "key.key": "1",
                "events": [
                    EventFake(event_type=keyboard.KEY_DOWN, name="alt"),
                    EventFake(event_type=keyboard.KEY_DOWN, name="1"),
                ],
                "result": True
            },
            {
                "mode": Mode(alt=True),
                "key.key": "1",
                "events": [
                    EventFake(event_type=keyboard.KEY_DOWN, name="alt"),
                    EventFake(event_type=keyboard.KEY_DOWN, name="2"),
                ],
                "result": False
            },
            # -----------------------------------------------------------------
        )

        for test_set in test_sets:

            key = Key(digits=True)
            key.key = test_set["key.key"]
            mode = test_set["mode"]
            sut = KeyCombo(mode=mode, key=key, legend=[], weight=1)
            threading.Thread(
                target=self._send_events,
                args=(sut, test_set["events"]),
            ).start()
            self.assertEqual(
                test_set["result"], sut.wait(), "Test failed")
            time.sleep(0.1)
            del sut


def main() -> None:
    """Run all tests in KeyComboTest."""
    _ = KeyComboTest()
    unittest.main()


if __name__ == "__main__":
    main()
