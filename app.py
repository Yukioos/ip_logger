from flask import Flask, request, render_template
import requests

app = Flask(__name__)

BOT_TOKEN = '8439041030:AAFK7c9-xia3_fWtY4mMzorWfKuVWgRSnf4'
CHAT_ID = '774044847'

def send_telegram_message(ip, geo_info):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': f'Новый посетитель сайта с IP: {ip} {geo_info}'}
    requests.post(url, data=data)

@app.route('/')
def index():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.remote_addr
    geo_info = get_geo_info(ip)
    send_telegram_message(ip)

    return render_template('index.html')

def get_geo_info(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        if data['status'] == 'success':
            country = data.get('country', 'Unknown')
            city = data.get('city', 'Unknown')
            return f'{country}, {city}'
        else:
            return 'Geo info not available'
    except:
        return 'Geo lookup failed'


if __name__ == '__main__':
    app.run(debug=True)
