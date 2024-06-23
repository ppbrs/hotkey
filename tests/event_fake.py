"""EventFake class."""
import keyboard  # type: ignore


class EventFake:  # pylint: disable=R0903
    """Fake keyboard event (keyboard.KeyboardEvent) for testing Key_combo callback."""

    def __init__(
        self,
        event_type: str,  # keyboard.KEY_DOWN | keyboard.KEY_UP
        name: str,
    ) -> None:

        assert event_type in (keyboard.KEY_DOWN, keyboard.KEY_UP)
        self.event_type = event_type
        self.name = name

    def __repr__(self) -> str:
        type_repr = 'unknown'
        if self.event_type == keyboard.KEY_DOWN:
            type_repr = 'dn'
        if self.event_type == keyboard.KEY_UP:
            type_repr = 'up'
        return f'Event({type_repr}, {self.name})'
