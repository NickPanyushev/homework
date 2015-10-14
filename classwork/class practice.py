class Song:
    def __init__(self, artist, name):
        self.artist = artist
        self.name = name
    def __repr__(self):
        song = "Song \"%s\" by  %s" % (self.name, self.artist)
        return song
    def __lt__ (self, other):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.name < other.name:
            return True
        return False
def filter_sorted (songs, word):
        good_songs = []
        word = word.lower()
        for song in songs:
            if word in song.artist.lower() or word in song.name.lower():
                good_songs.append(song)
        return good_songs
        
#song1 = Song ("Frank Zappa", "Bobby brown goes down")
#song2 = Song ("Petula Clark", "I know a place")
input_file = open("songs_shuffled.txt", "r")
lines = input_file.readlines()

songs = []
n = int(lines[0])
for i in range(n):
    artist, name = lines[1+i][:-1].split("-")
    songs.append(Song(artist, name))
#for song in songs:
    #print (song)
input_file.close()
# print (song2)

for song in filter_sorted(songs, "of"):
    print(song)
