import unittest
import ipv4

class TestIPv4(unittest.TestCase):

    def test_valid_ip(self):
        self.assertTrue(ipv4.is_valid_ipv4("192.168.1.1"))

    def test_invalid_ip_letters(self):
        self.assertFalse(ipv4.is_valid_ipv4("192.abc.1.1"))

    def test_invalid_ip_range(self):
        self.assertFalse(ipv4.is_valid_ipv4("256.1.1.1"))

    def test_invalid_ip_parts(self):
        self.assertFalse(ipv4.is_valid_ipv4("192.168.1"))

if __name__ == "__main__":
    unittest.main()
