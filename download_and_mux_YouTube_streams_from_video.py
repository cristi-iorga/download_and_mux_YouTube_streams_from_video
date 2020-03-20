"""

Name:     download_and_mux_YouTube_streams_from_video
Purpose:  Lets you choose a video and an audio stream from a YouTube video link and muxes them together using ffmpeg
Author:   iorga.ton@gmail.com
Revision: 20.03.2020 - initial version 

Python Version:  3.8.2
Windows Version: 10.0.17763

Dependencies: pytube (pip install pytube3)
			  ffmpeg 

"""

from pytube import YouTube
import os
import sys
import time

def get_input():
	input_link = input("\nEnter the Youtube link here and press ENTER: ")
	return input_link

def choose_muxed_stream():
	input_tag = input("\nChoose an itag to download and press ENTER to start downloading: ")
	return input_tag

def choose_video_audio_stream():

	video_tag = input("\nChoose an itag for the VIDEO stream and press ENTER: ")
	audio_tag = input("\nChoose an itag for the AUDIO stream and press ENTER: ")
	only_audio_question = input("\nWould you like audio only? (y/n)")

	if only_audio_question == "y":
		only_audio = True
	elif only_audio_question == "n":
		only_audio = False
	else:
		print("Invalid input! I'm assuming you don't care, we'll do both then")
		only_audio = False

	return (video_tag, audio_tag, only_audio)

def display_muxed_streams(video):

	print("\nThese are all the available muxed streams:\n")
	muxed_list = (video.streams.filter(progressive=True))
	print(*muxed_list, sep="\n")

def display_video_streams(video):

	print("\nThese are all the available video streams:\n")
	video_list = (video.streams.filter(only_video=True))
	print(*video_list, sep="\n")

def display_audio_streams(video):
	print("\nThese are all the available audio streams:\n")
	audio_list = (video.streams.filter(only_audio=True))
	print(*audio_list, sep="\n")

def download_streams():
	link = get_input()
	video = YouTube(link)

	display_muxed_streams(video)
	display_video_streams(video)
	display_audio_streams(video)

	video_tag, audio_tag, only_audio = choose_video_audio_stream()

	output_path_video = None

	if not only_audio:

		video_stream = video.streams.get_by_itag(video_tag)
		output_path_video = video_stream.download(filename_prefix="video_")
	
	audio_stream = video.streams.get_by_itag(audio_tag)
	output_path_audio = audio_stream.download(filename_prefix="audio_")

	full_video_name = video.title


	return(output_path_video, output_path_audio, full_video_name, only_audio)

def add_doublequotes(command):
	
	quoted_command = '"' + str(command) + '"'

	return quoted_command

def file_muxer(video_file, audio_file, full_name):

	try:
		video_file_name = os.path.basename(video_file)
		video_file_root, video_file_extension = os.path.splitext(video_file_name)
		audio_file_name = os.path.basename(audio_file)
		audio_file_root, audio_file_extension = os.path.splitext(audio_file_name)

		video_file = add_doublequotes(video_file)
		audio_file = add_doublequotes(audio_file)
	
		in_video_file = add_doublequotes(video_file_name)
		in_audio_file = add_doublequotes(audio_file_name)

		out_file = add_doublequotes(full_name + video_file_extension)

		print("Video file is: ", video_file_name)
		print("Audio file is: ", audio_file_name)

		mux_files = 'ffmpeg -i ' + video_file + ' -i ' + audio_file + ' -vcodec copy -acodec copy -map 0:0 -map 1:0 ' + out_file

		print(mux_files)

		os.system(mux_files)

	except OSError as err:
		print(err.reason)
		exit(1)

if __name__ == '__main__':

	# downloads the two streams:

	video_path, audio_path, full_name, only_audio = download_streams()

    # muxes the two streams that were downloaded into a new file and deletes the original files

	if not only_audio:

		file_muxer(video_path, audio_path, full_name)
		
		os.remove(video_path)
		os.remove(audio_path)

	input("\n\nDone! Press any key to exit!")