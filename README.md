# YouTube Sentiment Analysis

This project is a YouTube sentiment analysis tool that fetches comments from a specified YouTube video and performs sentiment analysis on the fetched comments. The goal of this project is to provide insights into viewer sentiments, which can be useful for content creators, marketers, and analysts.

## Features

- Fetch comments from any YouTube video using the YouTube Data API v3.
- Perform sentiment analysis on the comments using the TextBlob library.
- Display the results of the sentiment analysis, showing the distribution of positive, neutral, and negative comments.

## Requirements

### Software Requirements

- Python 3.6 or higher
- Virtual Environment (venv)
- Google API Key (YouTube Data API v3)

### Libraries

All required libraries are listed in the `requirements.txt` file. They include:

- `google-api-python-client`
- `python-dotenv`
- `textblob`

## Setup

### 1. Apply for a Google API Key

To use the YouTube Data API, you need to apply for an API key:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the YouTube Data API v3.
4. Create credentials for an API key.
5. Save your API key securely.

### 2. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/
cd youtube-sentiment-analysis
```

### 3. Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a .env file in the root directory of your project and add your YouTube API key:

```bash
source .env
```

```plaintext
YOUTUBE_API_KEY=your_api_key_here
```


## Usage

### Running the Script
Replace the video_id in the script with the ID of the YouTube video you want to analyze. Then run the script:

```bash
python youtube_sentiment_analysis.py
```








