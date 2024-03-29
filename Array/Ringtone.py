from colorama import Fore
from playsound import playsound
from plyer import notification


print("Available songs:\n")
songs = ["Dil mai ho tum", "Tim-Tim"]
song_files = [
    r"D:\C DATA\DESKTOP\Python\PythonDSAProject\Array\Songs\dil-mai-ho-tum.mp3",
    r"D:\C DATA\DESKTOP\Python\PythonDSAProject\Array\Songs\allvideo-1705652469836-61724.mp3",
]

for song in songs:
    print(song)

print("<----- Choose your favourite ringtone ----->")
fav = input("Enter the name of your favorite ringtone: ")


def songSelection():
    if fav in songs:
        # Get the index of the selected song
        index = songs.index(fav)

        # Get the corresponding file name
        song_file = song_files[index]

        try:
            # Play the selected song
            playsound(song_file)

        except Exception as e:
            print(Fore.RED + f"Error playing the ringtone: {e}")
        else:

            print(Fore.YELLOW + "Your favorite ringtone has been selected")
            notification.notify(
                title="Ringtone Selected",
                message=f"Playing: {song_file}",
                timeout=5,
            )
    else:
        print(Fore.RED + "Sorry, the song is not available.")
        # Show notification for unavailable song
        notification.notify(
            title=f"======>OOPS!  <======",
            message="Your favorite ringtone is not there!! Sorry",
            timeout=5,
        )


songSelection()
