import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.instance_of_room = Room(1)
        self.instance_of_song = Song ("Hurricane", "Bob Dylan")
        self.another_instance_of_song = Song("All along the watchtower", "Bob Dylan")
        self.instance_of_guest = Guest("Stephen", 100, self.instance_of_song)

    
    def test_room_has_number(self):
        self.assertEqual(1, self.instance_of_room.room_number)

    def test_check_in(self):
        self.instance_of_room.check_in(self.instance_of_guest)
        is_in_room = self.instance_of_guest in self.instance_of_room.checked_in_guests
        self.assertEqual(True, is_in_room)
        self.assertEqual(True, self.instance_of_guest.is_checked_in)
        self.assertEqual(90, self.instance_of_guest.money)

    def test_check_out(self):
        self.instance_of_room.check_in(self.instance_of_guest)
        self.instance_of_room.check_out(self.instance_of_guest)
        is_in_room = self.instance_of_guest in self.instance_of_room.checked_in_guests
        self.assertEqual(False, is_in_room)
        self.assertEqual(False, self.instance_of_guest.is_checked_in)

    def test_add_song_to_room(self):
        self.instance_of_room.add_song(self.instance_of_song, self.instance_of_room)
        # is_song_added_to_room = self.instance_of_song in self.instance_of_room.songs
        self.assertEqual(1, len(self.instance_of_room.songs))

    def test_refuse_check_in(self):
        self.instance_of_room.checked_in_guests = ["Mike", "Jude", "Laura"]
        self.instance_of_room.check_in(self.instance_of_guest)
        self.assertEqual(3, len(self.instance_of_room.checked_in_guests))

    def test_favourite_song_is_in_room(self):
        self.instance_of_room.add_song(self.instance_of_song, self.instance_of_room)
        self.instance_of_room.check_in(self.instance_of_guest)
        self.assertEqual("Wooh!", self.instance_of_room.check_in(self.instance_of_guest))

        