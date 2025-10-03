from playlist import Playlist
from utils import get_input, print_divider

def menu():
    print_divider()
    print("🎵 Music Playlist Manager")
    print("1. Add Song")
    print("2. Remove Song")
    print("3. Search Song")
    print("4. Show All Songs")
    print("5. Exit")
    print_divider()

def main():
    playlist = Playlist()

    while True:
        menu()
        choice = get_input("Enter choice: ")

        if choice == "1":
            title = get_input("Enter song title: ")
            artist = get_input("Enter artist name: ")
            duration = get_input("Enter duration (mins): ")
            playlist.add_song(title, artist, duration)

        elif choice == "2":
            title = get_input("Enter title to remove: ")
            playlist.remove_song(title)

        elif choice == "3":
            keyword = get_input("Enter keyword to search: ")
            results = playlist.search(keyword)
            if results:
                print("🔍 Results:")
                for song in results:
                    print(song)
            else:
                print("❌ No matches found.")

        elif choice == "4":
            playlist.show_all()

        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
