class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_song(self):
        for x in self.lyrics:
            print(x)


music = Song(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])

music.sing_me_song()