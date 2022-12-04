import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.instance_of_room = Room("Red", 3)
        self.instance_of_song = Song ("Hurricane", "Bob Dylan")
        self.instance_of_song_2 = Song("All along the watchtower", "Bob Dylan")
        self.instance_of_song_3 = Song("Theme de yoyo", "Art ensamble of Chicago")
        self.instance_of_guest = Guest("Stephen", 100, self.instance_of_song)
        self.instance_of_guest_2 = Guest("Peter", 75, self.instance_of_song_2)
        self.instance_of_guest_3 = Guest("Lucy", 120, self.instance_of_song_2)
        self.instance_of_guest_4 = Guest("Ben", 80, self.instance_of_song_3 )

    
    def test_room_has_name(self):
        self.assertEqual("Red", self.instance_of_room.room_number)

    def test_check_in(self):
        self.instance_of_room.check_in(self.instance_of_guest)
        self.assertEqual(1, len(self.instance_of_room.checked_in_guests))
        self.assertEqual(True, self.instance_of_guest.is_checked_in)
        self.assertEqual(90, self.instance_of_guest.money)

    def test_check_out(self):
        self.instance_of_room.check_in(self.instance_of_guest)
        self.instance_of_room.check_out(self.instance_of_guest)
        self.assertEqual(0, len(self.instance_of_room.checked_in_guests))
        self.assertEqual(False, self.instance_of_guest.is_checked_in)

    def test_add_song_to_room(self):
        self.instance_of_room.add_song(self.instance_of_song, self.instance_of_room)
        self.assertEqual(1, len(self.instance_of_room.songs))

    def test_refuse_check_in(self):
        self.instance_of_room.checked_in_guests = [self.instance_of_guest_2, self.instance_of_guest_3, self.instance_of_guest_4]
        self.instance_of_room.check_in(self.instance_of_guest)
        self.assertEqual(3, len(self.instance_of_room.checked_in_guests))

    def test_favourite_song_is_in_room(self):
        self.instance_of_room.add_song(self.instance_of_song, self.instance_of_room)
        self.instance_of_room.check_in(self.instance_of_guest)
        self.assertEqual("Wooh!", self.instance_of_room.check_in(self.instance_of_guest))

        