from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '8439041030:AAFK7c9-xia3_fWtY4mMzorWfKuVWgRSnf4'
CHAT_ID = '774044847'

def send_telegram_message(text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, data=data)

@app.route('/')
def index():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.remote_addr

    send_telegram_message(f'Новый посетитель сайта с IP: {ip}')

    return "Добро пожаловать на сайт!"

if __name__ == '__main__':
    app.run(debug=True)