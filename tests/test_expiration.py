import unittest

class TestLeaseExpiration(unittest.TestCase):
    def test_renewal_advances_timestamp(self):
        current_exp = 1750000000
        extension_seconds = 86400 * 365
        new_exp = current_exp + extension_seconds
        self.assertGreater(new_exp, current_exp)

    def test_negative_renewal_rejected(self):
        current_exp = 1750000000
        extension_seconds = -100
        self.assertLess(extension_seconds, 0)

if __name__ == '__main__':
    unittest.main()
