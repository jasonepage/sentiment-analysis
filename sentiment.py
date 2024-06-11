from textblob import TextBlob
from dotenv import load_dotenv
import os
# visualize the sentiment analysis results
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


class SentimentAnalyzer:
    def __init__(self, api_key):
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("No API key found. Please check your .env file.")

        
    def analyze_comments(self, comments):
        """
        Analyze the sentiment of the comments
        """
        sentiments = {
            'positive': 0,
            'neutral': 0,
            'negative': 0
        }
        for comment in comments:
            blob = TextBlob(comment)
            sentiment = blob.sentiment.polarity
            if sentiment > 0:
                sentiments['positive'] += 1
            elif sentiment == 0:
                sentiments['neutral'] += 1
            else:
                sentiments['negative'] += 1
        return sentiments
    
    def visualize_sentiments(self, sentiments):
        """
        Visualize the sentiment analysis results.
        
        """
        labels = list(sentiments.keys())
        values = list(sentiments.values())
        colors = ['green', 'yellow', 'red']
        
        plt.figure(figsize=(10, 6))
        plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Sentiment Analysis Results')
        plt.show()


