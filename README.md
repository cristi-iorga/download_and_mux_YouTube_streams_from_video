# download_and_mux_YouTube_streams_from_video

### Overview:

Language: Python

Requirements: ffmpeg
              pytube3 (pip install pytube3)

Input Mode: terminal

Output folder: same as input

Output name: - same as video title - (with an "audio_" prefix if audio only is chosen)

General concept: pick and choose the streams from the video and mux them in a container

### How to use

You need to install pytube first, open a terminal windows and type:

`pip install pytube3`

Also, check if you have ffmpeg installed on your machine (https://www.ffmpeg.org/). It is required for the process of muxing a video and an audio stream together.

This script takes the link to a YouTube video that you input and displays all the available streams. You can choose to download a specific video and a specific audio stream and have the programm automatically mux them together. You can also download only an audio stream if you so desire.

#### Enjoy!
