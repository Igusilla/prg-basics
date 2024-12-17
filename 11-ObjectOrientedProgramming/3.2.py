# class definition
class Song:
   def __init___(self):
      self.artist = ""
      self.track_title = ""
      self.album = ""
      self.year = 0

   def __str__(self):
      return f"Performer: {self.artist}\nTitle: {self.track_title}\nAlbum: {self.album}\nYear: {self.year}"

# object creation
song1 = Song()
song1.artist = "Ed Sheeran"
song1.track_title = "Celestials"
song1.album = "Pokemon"
song1.year = 2023
song2 = Song()
song2.artist = "Kendrick Lamar"
song2.track_title = "Not Like Us"
song2.album = "IDK"
song2.year = 2024


## object usage
print(song1)
print(song2)