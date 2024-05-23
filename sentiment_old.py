# Author(s): Jason Page
# Date: 5/10/2024
# Description: This file contains the sentiment analysis functions for the project.

import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('YOUTUBE_API_KEY')

# Set up the YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

print('YouTube API client successfully set up!')

def get_video_details(video_id):
    try:
        request = youtube.videos().list(
            part='snippet,contentDetails,statistics',
            id=video_id
        )
        response = request.execute()
        
        if not response['items']:
            print(f'No video found with ID: {video_id}')
            return
        
        for item in response['items']:
            title = item['snippet']['title']
            description = item['snippet']['description']
            view_count = item['statistics']['viewCount']
            like_count = item['statistics']['likeCount']
            comment_count = item['statistics']['commentCount']
            duration = item['contentDetails']['duration']
            
            print(f'Title: {title}')
            print(f'Description: {description}')
            print(f'Views: {view_count}')
            print(f'Likes: {like_count}')
            print(f'Comments: {comment_count}')
            print(f'Duration: {duration}')
    except Exception as e:
        print(f'An error occurred: {e}')

# Replace with the ID of the YouTube video you want to fetch details for
video_id = 'SWJmH3YcXk4'
get_video_details(video_id)
