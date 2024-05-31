# Author(s): Jason Page
# Date: 5/10/2024
# Description: This file is the main file for the program. It will run the program and call the necessary functions to track social media sentiment.

import os, sys, time
from scraper import Scraper
from sentiment import get_video_comments, analyze_comments

def main():
    # Get the video ID from the command line arguments
    if len(sys.argv) < 2:
        print('Usage: python main.py <video_id>')
        sys.exit(1)
    
    video_id = sys.argv[1]
    
    # Scrape comments from the video
    print(f'Scraping comments for video ID: {video_id}')
    comments = get_video_comments(video_id)
    
    if not comments:
        print('No comments found. Exiting program.')
        sys.exit(1)
    
    # Analyze the comments
    print('Analyzing comments...')
    sentiments = analyze_comments(comments)
    
    # Print the sentiment analysis results
    print('Sentiment analysis results:')
    print(f'Positive comments: {sentiments["positive"]}')
    print(f'Neutral comments: {sentiments["neutral"]}')
    print(f'Negative comments: {sentiments["negative"]}')

