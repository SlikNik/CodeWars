import unittest

from katas.kyu_7.lorraine_wants_to_win_tv_contest import unscramble


class UnscrambleTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(unscramble('shi'), ['his'])

    def test_equals_2(self):
        self.assertEqual(unscramble('nowk'), ['know'])

    def test_equals_3(self):
        self.assertEqual(unscramble('amle'), ['male', 'meal'])
