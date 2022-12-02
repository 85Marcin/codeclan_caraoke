import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.instance_of_guest = Guest("Stephen")

    def test_guest_has_name(self):
        self.assertEqual("Stephen", self.instance_of_guest.name)

    