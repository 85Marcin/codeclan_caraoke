class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.checked_in_guests = []
        self.songs = []

    def check_in(self, guest):
        if len(self.checked_in_guests) < 3:
            guest.is_checked_in = True
            self.checked_in_guests.append(guest)
            guest.money -= 10 # entry fee
            for song in self.songs:
                if guest.favourite_song == song:
                    return "Wooh!"

    def check_out(self, guest):
        guest.is_checked_in = False
        self.checked_in_guests.remove(guest)

    def add_song(self, song, room):
        room.songs.append(song)
       