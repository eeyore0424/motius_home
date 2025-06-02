import os
from dotenv import load_dotenv

load_dotenv('.env')

SLACK_APP_TOKEN = os.environ.get('SLACK_APP_TOKEN')
SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET')
SLACK_CHANNEL_ID = os.environ.get('SLACK_CHANNEL_ID')
