import unittest
from context import core

class ExampleTest(unittest.TestCase):
    """An example test in unittest fashion."""
    def setUp(self):
        pass

    def test_will_pass(self):
        self.assertEqual(1, 1)

    def test_will_not_pass(self):
        self.assertEqual(1, 1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
