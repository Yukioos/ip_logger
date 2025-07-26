from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        # Берём первый IP из списка, если прокси несколько
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.remote_addr
    return f'Ваш IP: {ip}'

@app.route('/headers')
def headers():
    headers = dict(request.headers)
    # Красиво выводим все заголовки в теле ответа
    return "<pre>" + "\n".join(f"{k}: {v}" for k, v in headers.items()) + "</pre>"

if __name__ == '__main__':
    app.run(debug=True)