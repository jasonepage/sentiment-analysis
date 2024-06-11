import os
from scraper import Scraper
from sentiment import SentimentAnalyzer
from dotenv import load_dotenv

def main():
    # Load the API key from the .env file
    load_dotenv()
    api_key = os.getenv('YOUTUBE_API_KEY')
    if not api_key:
        raise ValueError("No API key found. Please check your .env file.")
    
    # Initialize the Scraper and SentimentAnalyzer
    scraper = Scraper(api_key)
    analyzer = SentimentAnalyzer()
    
    # Get comments from a YouTube video
    video_id = 'ek2yOqAIYuU' # TODO: Make this dynamic by automatically fetching the video IDs using 
    # 
    comments = scraper.get_video_comments(video_id)
    
    # Analyze the sentiment of the comments
    sentiments = analyzer.analyze_comments(comments)
    
    # Print the sentiment analysis results
    print('Sentiment Analysis Results:')
    print(f'Positive: {sentiments["positive"]}')
    print(f'Neutral: {sentiments["neutral"]}')
    print(f'Negative: {sentiments["negative"]}')
    
if __name__ == '__main__':
    main()
