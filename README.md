# YTViral - YouTube Video Viral Moments Extractor

## Overview

YTViral is a Streamlit web application designed to help users extract potentially viral moments from YouTube videos. It automatically downloads a YouTube video, analyzes it to find the most engaging segment, and then extracts a 30-second clip from that segment. This tool is perfect for content creators, marketers, or anyone looking to highlight key moments from a video.

## Features

- **YouTube Video Download**: Downloads the highest quality version of the specified YouTube video using `yt-dlp`.
- **Engagement Analysis**: Uses heuristic patterns to estimate the most-watched or engaging moments within the video.
- **Clip Extraction**: Extracts a 30-second clip from the estimated most-watched moment.
- **Simple UI**: A user-friendly interface built with Streamlit.

## Installation

To run this application locally, you need to have Python installed along with the required packages.

1. **Clone the repository**:
   \```bash
   git clone https://github.com/oussema68/YTViral.git
   cd YTViral
   \```

2. **Install the required packages**:
   \```bash
   pip install -r requirements.txt
   \```

3. **Run the Streamlit app**:
   \```bash
   streamlit run app.py
   \```

## Usage

1. **Input the YouTube URL**: Paste the YouTube video link into the input field.
2. **Download and Extract**: Click the "Download and Extract Clip" button. The app will download the video, determine the most engaging moment, and extract a 30-second clip from that point.
3. **Download the Clip**: Once the clip is extracted, you can download it directly from the app.

## Code Structure

- **`app.py`**: Main application file containing the Streamlit code.
- **`logo/logo.png`**: Logo image displayed in the app's header.

## Key Functions

- `download_video_with_ytdlp(url, output_name)`: Downloads the YouTube video using `yt-dlp`.
- `get_most_watched_time(video_url)`: Estimates the most-watched time based on heuristic patterns.
- `extract_clip(video_path, start_time, duration, output_name)`: Extracts a 30-second clip from the video.

## Dependencies

- `streamlit`
- `yt-dlp`
- `moviepy`
- `pytube`
- `numpy`

## Notes

- The application currently uses a heuristic-based approach to determine the most-watched time, which may not be 100% accurate but provides a reasonable estimate.
- Ensure you have `yt-dlp` installed and accessible from your system's PATH.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For any inquiries or support, please contact [ohammadi.oh@gmail.com](mailto:ohammadi.oh@gmail.com).
