import json

BAIDU_API_CONFIG_FILE = '.baidu_api_config.json'
NEWS_FILE = 'data/news.json'
AUDIO_FILE = 'data/audio.json'

def load_baidu_api_config():
    with open(BAIDU_API_CONFIG_FILE, 'r') as f:
        config = json.load(f)
        return config


def load_news():
    with open(NEWS_FILE, 'r') as f:
        news = json.load(f)
        return news
