from colorama import Fore
from playsound import playsound
import time
from plyer import notification

# Import the necessary Bootstrap components
html_head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ringtone Selector</title>
    <!-- Bootstrap CSS link -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <h1 class="text-center mb-4">Ringtone Selector</h1>
"""

html_tail = """
    </div>
    <!-- Bootstrap JS and Popper.js links -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
"""

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
