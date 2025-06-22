# Usage:
`python vlc-dub.py <video_folder> <dub_folder>`

EXAMPLE:
`python vlc-dub.py "C:\movies\bladerunner" "C:\dubs\bladerunner"`

# Conditions:
0. vlc is at "C:\Program Files\VideoLan\VLC\vlc.exe"

1. dub files have the same or prefixed/suffixed name as in: **Bladerunner_77**.mp4 -> **Bladerunner_77**_fr_dub.mp3 / 
The core name should remain the same

2. video files are recognised as either .mp4 or .mov files

3. dub files are recognised as either .mp3, .m4a, .wav, .flac, or .ogg

If dub files are in the same folder as the videos, pass just the videos folder
