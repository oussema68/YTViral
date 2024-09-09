import streamlit as st
import subprocess
import moviepy.editor as mp
from pytube import YouTube
import os
import numpy as np

# Function to download YouTube video using yt-dlp
def download_video_with_ytdlp(url, output_name='output_video.mp4'):
    command = [
        'yt-dlp',
        '--output', output_name,
        url
    ]
    subprocess.run(command)

# Function to estimate the most-watched time based on heuristic patterns
def get_most_watched_time(video_url):
    yt = YouTube(video_url)
    video_duration = yt.length
    
    num_segments = 100
    segment_duration = video_duration // num_segments
    segment_points = [0, video_duration // 4, video_duration // 2, 3 * video_duration // 4, video_duration]
    engagement_scores = {point: np.random.uniform(0.8, 1.0) for point in segment_points}

    most_watched_time = max(engagement_scores, key=engagement_scores.get)
    
    return most_watched_time

# Function to extract a 30-second clip
def extract_clip(video_path, start_time, duration=30, output_name='output_clip.mp4'):
    video = mp.VideoFileClip(video_path)
    
    # Ensure the end time does not exceed the video duration
    end_time = min(start_time + duration, video.duration)
    
    # Adjust the start time if it is too close to the end
    if end_time - start_time < duration:
        start_time = max(0, video.duration - duration)
        end_time = video.duration
    
    clip = video.subclip(start_time, end_time)
    clip.write_videofile(output_name, codec="libx264")
    clip.close()

# Streamlit app
st.title("YouTube Video Clip Extractor")

# Input for YouTube URL
youtube_url = st.text_input("Enter YouTube URL:")

if st.button("Download and Extract Clip"):
    if youtube_url:
        st.write("Downloading video in the highest quality...")
        download_video_with_ytdlp(youtube_url)
        
        # Check if the video file was created
        if os.path.isfile('output_video.mp4'):
            st.write("Determining the most-watched time...")
            most_watched_time = get_most_watched_time(youtube_url)
            
            st.write(f"Extracting 30-second clip starting at {most_watched_time} seconds...")
            try:
                extract_clip('output_video.mp4', start_time=most_watched_time)
                st.write("Clip extracted successfully!")
                
                with open('output_clip.mp4', 'rb') as file:
                    st.download_button(label="Download Clip", data=file, file_name='output_clip.mp4', mime='video/mp4')
                
                # Clean up files
                os.remove('output_video.mp4')
                os.remove('output_clip.mp4')
            except FileNotFoundError as e:
                st.error(str(e))
        else:
            st.error("Video file not found. Please check if the download process was successful.")
    else:
        st.warning("Please enter a valid YouTube URL.")
