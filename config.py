import os

class Config:
    REDDIT_CLIENT_ID = os.environ['REDDIT_CLIENT_ID']
    REDDIT_CLIENT_SECRET = os.environ['REDDIT_CLIENT_SECRET']
    REDDIT_USER_AGENT = os.environ['REDDIT_USER_AGENT']
    FLASK_PORT = int(os.environ.get('FLASK_PORT', 5000))
    GEMINI_API_KEY = os.environ['GEMINI_API_KEY']
    
    MONITORED_SUBREDDITS = [
        'worldnews', 'technology', 'science', 'business', 'politics',
        'news', 'economics', 'environment', 'health', 'education',
        'space', 'artificial', 'programming', 'startups', 'investing'
    ]
    
    NEWS_KEYWORDS = {
        'breaking': 10,
        'urgent': 9,
        'exclusive': 8,
        'first': 7,
        'major': 6,
        'significant': 5,
        'important': 4,
        'new': 3,
        'update': 2,
        'report': 1
    }
