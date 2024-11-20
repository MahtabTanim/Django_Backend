import random


class CoinFlips:
    def __init__(self, number_of_flips):
        self.number_of_flips = number_of_flips
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number_of_flips:
            self.counter += 1
            return random.choice(["T", "H"])
        raise StopIteration


# x = CoinFlips(10)
#
# for flip in x:
#     print(flip)


class Playlist:
    def __init__(self, songs, shuffle=False):
        self.songs = songs
        self.index = 0

        if shuffle:
            random.shuffle(self.songs)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.songs):
            raise StopIteration

        print(f"Playing {self.songs[self.index]}")
        self.index += 1


# x = Playlist(['19', '12', '11'], True)
# for song in x:
#     print(song)

songs = ["Hooked on a Feeling", "Yesterday", "Mr. Blue Sky"]
classic_rock_playlist = Playlist(songs, shuffle=True)


# while True:
#     try:
#         # Play the next song in the playlist
#         next(classic_rock_playlist)
#
#     # If there is a StopIteration error, print a message and
#     # stop the playlist
#     except StopIteration:
#         print("Reached end of playlist!")
#         break


class Lottery:
    def __init__(self, number_digits):
        self.number_digits = number_digits
        self.counter = 0

    def __iter__(self):
        return self

    # Check if the number of digits have been reached, or else
    # pull another number
    def __next__(self):
        if self.counter < self.number_digits:
            self.counter += 1
            return random.randint(0, 9)
        raise StopIteration


charity_lottery = Lottery(4)

# Announce all four numbers
while True:
    try:
        print(next(charity_lottery))
    # Handle the last element of the iterator, print a message
    except StopIteration:
        print("... is the winner!")
        break
