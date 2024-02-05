# Designing your Favourite ringtone

from colorama import Fore

# print(Fore.YELLOW + "hello world")
from playsound import playsound

print("Available songs:\n")
songs = ["Dil mai ho tum"]
song_files = ["D:\C DATA\DESKTOP\Python\PythonDSAProject\Array\Songs\dil-mai-ho-tum.mp3"]

for song in songs:
    print(song)

print("<----- Choose your favourite ringtone ----->")
fav = input()


def songSelection():

    if fav in songs:
        # Get the index of the selected song
        index = songs.index(fav)

        # Get the corresponding file name
        song_file = song_files[index]

        # Play the selected song
        playsound(song_file)
    else:
        print("Sorry, the song is not available.")


songSelection()
