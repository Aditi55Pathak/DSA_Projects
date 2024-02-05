from colorama import Fore
from playsound import playsound
import time
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

            while True:
                notification.notify(
                    title=f"======>{song_files[index]}  <======",
                    message="Your favorite ringtone is being played. Enjoy",
                    timeout=1,
                )
                time.sleep(5)
    else:
        print(Fore.RED + "Sorry, the song is not available.")
        while True:
            notification.notify(
                title=f"======>OOPS!  <======",
                message="Your favorite ringtone is not there!! Sorry",
                timeout=1,
            )
            time.sleep(5)


songSelection()
