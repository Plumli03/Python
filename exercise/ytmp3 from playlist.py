import ssl
from pytube import YouTube,Playlist
import os

# Ensure SSL context is properly set up
ssl._create_default_https_context = ssl._create_stdlib_context

# Directory save the downloaded files
download_directory = r'C:\Users\Hcedu\Desktop\python\mp3'

# Create a Playlist object
playlist = Playlist('https://www.youtube.com/playlist?list=PLINj2JJM1jxOxE-4mVaEJCEzO1CiR0Cwm')

video_list = [[vid.title, vid.watch_url] for vid in playlist.videos]
# enumerate index for songs
for i, (title, url) in enumerate(video_list):
    print(f'{i}, {title}: {url}')

# Specify the indices of videos to download
urls = [video_list[i][1] for i in [0,2,8,6,4]]
# urls = ['..',...]

for i in urls:
    try:
        # Create a YouTube object
        yt = YouTube(i)

        filename = f"{yt.author} - {yt.title}.mp3"
        file_path = os.path.join(download_directory, filename)

        # Download audio stream
        yt.streams.filter(only_audio=True).first().download(output_path=download_directory, filename=filename)
    except Exception as e:
        print(f'An error occurred:{e}')
print('All downloads completed!')


#------trim---------------
from pydub import AudioSegment

# Define the path to the MP3 file
file_path = r"C:\Users\Hcedu\Desktop\python\mp3\Taylor Swift - Fortnight.mp3"  # Replace 'yourfile.mp3' with the actual filename

# Open the MP3 file
song = AudioSegment.from_file(file_path, format="mp3")

# Define start and end times (in seconds)
t0, t1 = 5, 30

# Convert times to milliseconds
s = t0 * 1000
e = t1 * 1000

# Trim the song
trim = song[s:e]

# Define the output file path
output_file_path = file_path.replace('.mp3', '_trim.mp3')

# Save the trimmed audio
trim.export(output_file_path, format="mp3")

print("New Audio file is created and saved at:", output_file_path)
