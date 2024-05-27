# Author(s): Jason Page
# Date: 5/10/2024
# Description: This file contains the sentiment analysis functions for the project.

import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
from textblob import TextBlob

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('YOUTUBE_API_KEY')

if not api_key:
    raise ValueError("No API key found. Please check your .env file.")

# Set up the YouTube API client
try:
    youtube = build('youtube', 'v3', developerKey=api_key)
    print('YouTube API client successfully set up!')
except Exception as e:
    print(f'Error setting up YouTube API client: {e}')
    raise

def get_video_comments(video_id, max_results=100):
    try:
        comments = []
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=max_results,
            textFormat='plainText'
        )
        response = request.execute()

        while request is not None:
            response = request.execute()
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)
            request = youtube.commentThreads().list_next(request, response)

        return comments
    except Exception as e:
        print(f'An error occurred while fetching comments: {e}')
        return []

def analyze_comments(comments):
    sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}
    for comment in comments:
        analysis = TextBlob(comment)
        if analysis.sentiment.polarity > 0:
            sentiments['positive'] += 1
        elif analysis.sentiment.polarity == 0:
            sentiments['neutral'] += 1
        else:
            sentiments['negative'] += 1
    return sentiments
