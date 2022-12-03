import unittest
from classes.guest import Guest
from classes.song import Song
class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.instance_of_song = Song("Hurricane", "Bob Dylan")
        self.instance_of_guest = Guest("Stephen", 100, self.instance_of_song)
        

    def test_guest_has_name(self):
        self.assertEqual("Stephen", self.instance_of_guest.name)
    
    def test_guest_have_favourite_song(self):
        self.assertEqual(True, self.instance_of_guest.favourite_song == self.instance_of_song)
    