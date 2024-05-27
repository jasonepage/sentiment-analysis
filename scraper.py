# Author(s): Jason Page
# Date: 5/15/2024
# Description: This file contains the web scraping functions for the project. It scrapes data from youtube or other websites.

import os, requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
from dotenv import load_dotenv


class Scraper:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv
        if not self.api_key:
            raise ValueError("No API key found. Please check your .env file.")
        
    def get_video_comments(self, video_id, max_results=100):
        """
        Get comments from a YouTube video
        :param video_id: The ID of the YouTube video
        :param max_results: The maximum number of comments to retrieve
        :return: A list of comments
        """
        try:
            comments = []
            url = f'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&maxResults={max_results}&key={self.api_key}'
            response = requests.get(url)
            data = response.json()
            for item in data['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)
            return comments
        except Exception as e:
            print(f'An error occurred while fetching comments: {e}')
            return []
        
    def scrape_website(self, url):
        """
        Scrape a website for data
        :param url: The URL of the website to scrape
        :return: The scraped data
        """
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.find_all('p')
            return data
        except Exception as e:
            print(f'An error occurred while scraping the website: {e}')
            return []
        
    def analyze_data(self, data):
        """
        Analyze the scraped data
        :param data: The data to analyze
        :return: The analysis results
        """
        analysis = {}
        analysis['num_paragraphs'] = len(data)
        analysis['num_words'] = sum(len(p.text.split()) for p in data)
        analysis['num_characters'] = sum(len(p.text) for p in data)
        return analysis
