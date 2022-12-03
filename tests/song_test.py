import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.instance_of_song = Song("Hurricane", "Bob Dylan")
    def test_song_has_title(self):
        self.assertEqual("Hurricane", self.instance_of_song.title)

    def test_song_has_artist(self):
        self.assertEqual("Bob Dylan", self.instance_of_song.artist)

    


