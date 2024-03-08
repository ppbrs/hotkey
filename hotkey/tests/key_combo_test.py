"""


"""

import _thread
import keyboard
import time
import unittest
from unittest.mock import Mock

# this give access to the methods-under-test
# 1) when run directly
# 2) when run under nosetests
if __name__ == '__main__' and __package__ is None:
    import sys
    import os
    sut_path = os.path.dirname(os.path.normpath(os.path.join(__file__, '..')))
    print(f'appending `{sut_path}` to sys/path', sut_path)
    sys.path.append(sut_path)

    from event_fake import Event_fake
    from key_combo import Key_combo
    from key import Key
    from mode import Mode
else:
    from .event_fake import Event_fake
    from ..key_combo import Key_combo
    from ..key import Key
    from ..mode import Mode


class Key_combo_test(unittest.TestCase):

    def _send_events(self, key_combo, event_list):
        time.sleep(0.1)
        for event in event_list:
            # print('sending', event)
            key_combo.callback(event)
        pass

    def test_alt_key_ok(self):

        test_sets = (
            # -----------------------------------------------------------------
            # Without modifiers:
            # -----------------------------------------------------------------
            {
                'mode': Mode(),
                'key.key': 'a',
                'events':
                [
                    Event_fake(event_type=keyboard.KEY_DOWN, name='a'),
                ],
                'result': True
            },
            {
                'mode': Mode(),
                'key.key': 'a',
                'events':
                [
                    Event_fake(event_type=keyboard.KEY_DOWN, name='b'),
                ],
                'result': False
            },
            # -----------------------------------------------------------------
            # alt + smth
            # -----------------------------------------------------------------
            {
                'mode': Mode(alt=True),
                'key.key': '1',
                'events':
                [
                    Event_fake(event_type=keyboard.KEY_DOWN, name='alt'),
                    Event_fake(event_type=keyboard.KEY_DOWN, name='1'),
                ],
                'result': True
            },
            {
                'mode': Mode(alt=True),
                'key.key': '1',
                'events':
                [
                    Event_fake(event_type=keyboard.KEY_DOWN, name='alt'),
                    Event_fake(event_type=keyboard.KEY_DOWN, name='2'),
                ],
                'result': False
            },
            # -----------------------------------------------------------------
        )

        for test_set in test_sets:

            key = Key(digits=True)
            key.key = test_set['key.key']
            mode = test_set['mode']
            sut = Key_combo(mode=mode, key=key, log=Mock(), legend=[], weight=1)
            _thread.start_new_thread(self._send_events,
                                     (sut, test_set['events'], ))
            self.assertEqual(test_set['result'], sut.wait(),
                             'Test failed')
            time.sleep(0.1)
            del sut


def main():
    _ = Key_combo_test()
    unittest.main()


if __name__ == '__main__':
    main()
