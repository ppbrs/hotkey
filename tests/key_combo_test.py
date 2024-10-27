"""KeyComboTest class."""

import dataclasses
import logging
import threading
import time
from collections.abc import Iterable

import keyboard  # type: ignore

from hotkey.key import Key
from hotkey.key_combo import KeyCombo
from hotkey.mode import Mode

from .event_fake import EventFake

_logger = logging.getLogger(__name__)


@dataclasses.dataclass
class KeyComboTestCase:
    """Test case for KeyCombo."""

    mode: Mode
    key: Key
    events: list[EventFake]
    result: bool
    """Returned from KeyCombo.wait() after events are sent."""


key_combo_test_cases = [
    # -----------------------------------------------------------------
    # Without modifiers:
    # -----------------------------------------------------------------
    KeyComboTestCase(
        Mode(),
        Key(specific="a"),
        [
            EventFake(event_type=keyboard.KEY_DOWN, name="a"),
        ],
        True,
    ),
    KeyComboTestCase(
        Mode(),
        Key(specific="a"),
        [
            EventFake(event_type=keyboard.KEY_DOWN, name="b"),
        ],
        False,
    ),
    # -----------------------------------------------------------------
    # alt + smth
    # -----------------------------------------------------------------
    KeyComboTestCase(
        Mode(alt=True),
        Key(specific="1"),
        [
            EventFake(event_type=keyboard.KEY_DOWN, name="alt"),
            EventFake(event_type=keyboard.KEY_DOWN, name="1"),
        ],
        True,
    ),
    KeyComboTestCase(
        Mode(alt=True),
        Key(specific="1"),
        [
            EventFake(event_type=keyboard.KEY_DOWN, name="alt"),
            EventFake(event_type=keyboard.KEY_DOWN, name="2"),
        ],
        False,
    ),
    # -----------------------------------------------------------------
]


def test_key_combo():
    """
    Test that KeyCombo correctly reports captured pressed combinations.
    """

    def _send_events(
        key_combo: KeyCombo,
        event_list: Iterable[EventFake],
    ) -> None:
        """Call KeyCombo callbacks with the events from the provided list."""
        time.sleep(0.1)
        for event in event_list:
            _logger.debug("Sending event: %s.", event)
            key_combo.callback(event)

    for test_case in key_combo_test_cases:
        key_combo = KeyCombo(mode=test_case.mode, key=test_case.key, legend=[])
        _logger.info("Testing KeyCombo: %s.", key_combo)
        threading.Thread(
            target=_send_events,
            args=(key_combo, test_case.events),
        ).start()
        result = key_combo.wait()
        assert test_case.result == result, (
            f"Expected {test_case.result}, got {result}. "
            f"KeyCombo: {key_combo}. Sent events: {test_case.events}."
        )
        time.sleep(0.1)
        del key_combo
