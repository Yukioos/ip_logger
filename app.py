from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_ip():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return f'Ваш IP: {user_ip}'

if __name__ == '__main__':
    app.run()