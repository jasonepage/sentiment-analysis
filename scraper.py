import os
import requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
from dotenv import load_dotenv
from googleapiclient.discovery import build

class Scraper:
    def __init__(self, api_key):
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("No API key found. Please check your .env file.")
        
    def get_video_comments(self, video_id, max_results=100):
        """Get comments from a YouTube video"""
        try:
            comments = []
            youtube = build('youtube', 'v3', developerKey=self.api_key)
            response = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                maxResults=max_results
            ).execute()
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)
            return comments
        except Exception as e:
            print(f'An error occurred while fetching comments: {e}')
            return []
