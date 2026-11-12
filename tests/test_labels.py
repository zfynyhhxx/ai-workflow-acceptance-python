import unittest
from demo.labels import normalize_label

class LabelsTest(unittest.TestCase):
    def test_label(self):
        self.assertEqual(normalize_label("  Hello   WORLD "), "hello world")
