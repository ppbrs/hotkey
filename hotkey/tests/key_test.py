"""
"""

import unittest


from ..key import (Key, Key_error, )


class Key_test(unittest.TestCase):

    letters_list = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    digits_list = [chr(c) for c in range(ord('0'), ord('9') + 1)]
    symbols_list = ('`', '-', '=',
                    '[', ']', '\\',
                    ';', '\'',
                    ',', '.', '/',
                    'space')

    def setUp(self):
        """
        """
        self.assertEqual(len(self.symbols_list), 12, 'Symbols list not good')
        self.assertEqual(len(self.letters_list), 26, 'Letters list not good')
        self.assertEqual(len(self.digits_list), 10, 'Digits list not good')

    def tearDown(self):
        """
        """
        pass

    def test_letters(self):

        for _ in range(1000):
            sut = Key(letters=True)
            self.assertTrue(sut.key in self.letters_list,
                            'Key is not in valid range')

    def test_digits(self):

        for _ in range(1000):
            sut = Key(digits=True)
            self.assertTrue(sut.key in self.digits_list,
                            'Key is not in valid range')

    def test_symbols(self):

        for _ in range(1000):
            sut = Key(symbols=True)
            self.assertTrue(sut.key in self.symbols_list,
                            'Key is not in valid range')

    def test_chars(self):

        for _ in range(1000):
            sut = Key(chars=True)
            self.assertTrue(((sut.key in self.letters_list) or
                             (sut.key in self.digits_list) or
                             (sut.key in self.symbols_list)),
                            'Key is not in valid range')

    def test_esc(self):

        for _ in range(1000):
            sut = Key(esc=True)
            self.assertEqual(sut.key, 'esc',
                             'Key has wrong value')

    def test_llkbd(self):

        for _ in range(1000):
            sut = Key(llkbd=True)
            self.assertEqual(sut.key, 'llkbd',
                             'Key has wrong value')

    def test_backspace(self):

        for _ in range(1000):
            sut = Key(backspace=True)
            self.assertEqual(sut.key, 'backspace',
                             'Key has wrong value')

    def test_enter(self):

        for _ in range(1000):
            sut = Key(enter=True)
            self.assertEqual(sut.key, 'enter',
                             'Key has wrong value')

    def test_tab(self):

        for _ in range(1000):
            sut = Key(tab=True)
            self.assertEqual(sut.key, 'tab',
                             'Key has wrong value')

    def test_nonchars(self):

        for _ in range(1000):
            sut = Key(nonchars=True)
            self.assertTrue(((sut.key == 'esc') or
                             (sut.key == 'llkbd') or
                             (sut.key == 'backspace') or
                             (sut.key == 'enter') or
                             (sut.key == 'tab')),
                            'Key is not in valid range')

    def test_specific(self):

        test_sets = [

            ('a', 'a'), ('A', 'a'),
            ('z', 'z'), ('Z', 'z'),

            ('`', '`'), ('~', '`'),
            ('1', '1'), ('!', '1'),
            ('2', '2'), ('@', '2'),
            ('3', '3'), ('#', '3'),
            ('4', '4'), ('$', '4'),
            ('5', '5'), ('%', '5'),
            ('6', '6'), ('^', '6'),
            ('7', '7'), ('&', '7'),
            ('8', '8'), ('*', '8'),
            ('9', '9'), ('(', '9'),
            ('0', '0'), (')', '0'),
            ('-', '-'), ('_', '-'),
            ('=', '='), ('+', '='),
        ]

        for test_set in test_sets:
            sut = Key(specific=test_set[0])
            self.assertTrue(
                (sut.key == test_set[1]),
                msg=f'Key `{sut.key}` has unexpected value, `{test_set[1]}` is expected')

    def test_all(self):

        for _ in range(1000):
            sut = Key(letters=True,
                      digits=True,
                      symbols=True,
                      esc=True,
                      backspace=True,
                      enter=True)
            self.assertEqual(type(sut.key), str,
                             'Wrong type')
            self.assertTrue(((sut.key in self.digits_list) or
                             (sut.key in self.letters_list) or
                             (sut.key in self.symbols_list) or
                             (sut.key == 'esc') or
                             (sut.key == 'backspace') or
                             (sut.key == 'enter')),
                            'Key is not in valid range')

    def test_none(self):

        for _ in range(1000):
            with self.assertRaises(Key_error):
                Key()

    def test_compare(self):

        self.assertEqual(Key(esc=True),
                         Key(esc=True),
                         '`esc` must be equal to `esc`')
        self.assertEqual(Key(enter=True),
                         Key(enter=True),
                         '`enter` must be equal to `enter`')
        self.assertEqual(Key(backspace=True),
                         Key(backspace=True),
                         '`backspace` must be equal to `backspace`')
        self.assertNotEqual(Key(esc=True),
                            Key(backspace=True),
                            '')
        self.assertNotEqual(Key(esc=True),
                            Key(enter=True),
                            '')
        self.assertNotEqual(Key(enter=True),
                            Key(esc=True),
                            '')
        self.assertNotEqual(Key(enter=True),
                            Key(backspace=True),
                            '')
        self.assertNotEqual(Key(backspace=True),
                            Key(esc=True),
                            '')
        self.assertNotEqual(Key(backspace=True),
                            Key(enter=True),
                            '')

        sut_1 = Key(symbols=True)
        sut_2 = Key(symbols=True)
        sut_1.key = 'x'
        sut_2.key = 'X'
        self.assertEqual(sut_1, sut_2,
                         f'{str(sut_1)} must be equal to {str(sut_2)}')
        sut_1.key = 'X'
        sut_2.key = 'x'
        self.assertEqual(sut_1, sut_2,
                         f'{str(sut_1)} must be equal to {str(sut_2)}')

    def test_repr(self):

        self.assertEqual(str(Key(specific='l')), 'L')


def main():
    unittest.main()


if __name__ == '__main__':
    main()
