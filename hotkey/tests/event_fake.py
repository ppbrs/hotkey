"""


"""

import keyboard


class Event_fake:
    """
    Fake keyboard event for testing Key_combo callback.

    """
    def __init__(self, event_type=None, name=None):

        assert self._check_event_type(event_type), \
               "Missing or unsupported event type"

        assert self._check_name(name), \
               "Missing or unsupported event name"

        self.event_type = event_type
        self.name = name
        pass

    def _check_name(self, name):
        return name is not None

    def _check_event_type(self, event_type):
        return ((event_type == keyboard.KEY_DOWN) or (event_type == keyboard.KEY_UP))

    def __repr__(self):
        type_repr = 'unknown'
        if self.event_type == keyboard.KEY_DOWN:
            type_repr = 'dn'
        if self.event_type == keyboard.KEY_UP:
            type_repr = 'up'
        return f'Event({type_repr}, {self.name})'


if __name__ == '__main__':

    sut = Event_fake(event_type=keyboard.KEY_DOWN,
                     name='k')

    pass
