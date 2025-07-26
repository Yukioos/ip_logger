from flask import Flask, request

app = Flask(__name__)

IP_LOG_FILE = 'ips.txt'


def save_ip(ip):
    with open(IP_LOG_FILE, 'a') as f:
        f.write(ip + '\n')


@app.route('/')
def index():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.remote_addr

    save_ip(ip)
    return f'Ваш IP: {ip}'


if __name__ == '__main__':
    app.run(debug=True)