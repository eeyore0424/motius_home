from flask import Flask, render_template, jsonify, request
from .settings import *
from slack_sdk.errors import SlackApiError
from venv import logger
import json
import requests


def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def hello_motius():
        return render_template('index.html')
    
    @app.route('/terms')
    def terms():
        return render_template('terms.html')
    
    @app.route('/privacy')
    def privacy():
        return render_template('privacy.html')
    
    @app.route('/api/send-to-slack', methods=['POST'])
    def sendSlackBotMsg():
        print("SLACK BOT METHOD 진입")
        data = request.json
        name = data.get('name')
        phone = data.get('phone')
        content = data.get('content')

        message = f"📩 *새 문의 접수!*\n\n*이름:* {name}\n*연락처:* {phone}\n*내용:* {content}"


        token = SLACK_APP_TOKEN
        headers = {
            "Content-type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {token}"
        }

        payload = {
            "channel": SLACK_CHANNEL_ID,
            "text": message
        }

        data = {
            'token' : token,
            'channel' : SLACK_CHANNEL_ID,
            'text' : message,
        }
        try :
            URL = "https://slack.com/api/chat.postMessage"
            res = requests.post(URL, headers=headers,json=payload)
            print("Slack 응답 : ",res.text)

            if res.status_code == 200 and res.json().get('ok'):
                return jsonify({'status' : 'ok'}),200
            else :
                return jsonify({'status' : 'slack_error', 'message' : res.text}),500


        except SlackApiError as e:
            logger.error(f"Error posting message : {e}")
            return jsonify({'status':'fail', 'message' : str(e)}), 500
    
    return app