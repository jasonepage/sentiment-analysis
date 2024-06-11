import os
from scraper import Scraper
from sentiment import SentimentAnalyzer
from dotenv import load_dotenv

def main():
    """
    Main function to run the sentiment analysis on YouTube comments.

    """
    load_dotenv() # Load the API key from the .env file 
    api_key = os.getenv('YOUTUBE_API_KEY')
    if not api_key:
        raise ValueError("No API key found. Please check your .env file.")
    
    # Initialize the Scraper and SentimentAnalyzer
    scraper = Scraper(api_key)
    analyzer = SentimentAnalyzer(api_key)
    
    # Get video IDs from a YouTube channel
    channel_id = 'UC8butISFwT-Wl7EV0hUK0BQ' # freeCodeCamp channel
    video_ids = scraper.get_video_ids(channel_id)

    # Get comments from the first video
    video_id = video_ids[0]
    comments = scraper.get_video_comments(video_id)

    # Analyze the sentiment of the comments
    sentiments = analyzer.analyze_comments(comments)
    print(sentiments)

    # Visualize the sentiment analysis results
    analyzer.visualize_sentiments(sentiments)

if __name__ == '__main__':
    main()