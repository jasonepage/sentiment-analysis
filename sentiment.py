from textblob import TextBlob

class SentimentAnalyzer:
    def analyze_comments(self, comments):
        """Analyze the sentiment of the comments"""
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
