"""EventFake class."""

import dataclasses

import keyboard  # type: ignore


@dataclasses.dataclass
class EventFake:  # pylint: disable=R0903
    """
    Fake keyboard event (keyboard.KeyboardEvent) for testing KeyCombo wait and callback.

    Real keyboard.KeyboardEvent has more attributes, see
    https://github.com/boppreh/keyboard?tab=readme-ov-file#keyboard.KeyboardEvent
    """

    event_type: str
    """keyboard.KEY_DOWN | keyboard.KEY_UP"""
    name: str
    """E.g. 'a', '1', 'alt'"""

    def __init__(
        self,
        event_type: str,
        name: str,
    ) -> None:
        assert event_type in (keyboard.KEY_DOWN, keyboard.KEY_UP)
        self.event_type = event_type
        self.name = name

    def __repr__(self) -> str:
        type_repr = "unknown"
        if self.event_type == keyboard.KEY_DOWN:
            type_repr = "down"
        elif self.event_type == keyboard.KEY_UP:
            type_repr = "up"
        return f"{{{type_repr}, {self.name}}}"
