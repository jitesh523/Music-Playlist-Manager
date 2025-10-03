from song import Song

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, title, artist, duration):
        song = Song(title, artist, duration)
        self.songs.append(song)
        print(f"✅ Added: {song}")

    def remove_song(self, title):
        for song in self.songs:
            if song.title.lower() == title.lower():
                self.songs.remove(song)
                print(f"🗑️ Removed: {song}")
                return
        print("❌ Song not found!")

    def search(self, keyword):
        results = [song for song in self.songs if keyword.lower() in song.title.lower() or keyword.lower() in song.artist.lower()]
        return results

    def show_all(self):
        if not self.songs:
            print("🎶 Playlist is empty.")
        for idx, song in enumerate(self.songs, 1):
            print(f"{idx}. {song}")
