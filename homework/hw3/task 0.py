class Song:  # это все - конструктор класса
    def __init__(self, artist, name, album, track_number, year, duration):
        self.artist = artist
        self.name = name
        self.album = album
        self.track_number = track_number
        self.year = year
        self.duration = duration

    def __repr__(self):  # эта функция позволяет печатать красиво
        song = "Song \"%s\" by  %s in \"%s\" album " % (self.name, self.artist, self.album)
        return song

    def __lt__(self, other):  # эта функция сравнивает песни
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.name < other.name:
            return True
        return False


def filter_sorted(songs, word):
    good_songs = []
    word = word.lower()
    for song in songs:
        if word in song.artist.lower() or word in song.name.lower():
            good_songs.append(song)
    return good_songs


# song1 = Song ("Frank Zappa", "Bobby brown goes down", "prince", "34" , "2102" , "3 sec",  )
# song2 = Song ("Petula Clark", "I know a place")

def import_songs(file_name):
    with open(file_name, "r", encoding="utf8") as input_file:
        text = input_file.read()  # целиком считали файл
    lines = input_file.readlines()
    attributes = list (lines.split("\t"))
    # clean = [line for line in trash if line] #убрать пустое, не работает пока
    """songs = []
    for i in range (len(attributes)): # бежимся по листу, парсим по атрибутам песен
        artist, name, album, track_number, year, duration = attributes[i-1 : i+6]
        songs.append(Song(artist, name, album, track_number, year, duration))
    for song in songs:
        print(song)"""
    input_file.close()
    return (attributes)


print(import_songs("songs.txt"))

