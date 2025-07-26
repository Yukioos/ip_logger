from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # Получаем реальный IP из заголовка X-Forwarded-For (если есть)
    forwarded_for = request.headers.get('X-Forwarded-For', request.remote_addr)
    real_ip = forwarded_for.split(',')[0].strip()

    # Простая HTML-страница
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ваш IP</title>
        <meta charset="UTF-8">
        <style>
            body {{
                background-color: #f9f9f9;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }}
            .box {{
                background: #fff;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                display: inline-block;
            }}
            .ip {{
                font-size: 28px;
                font-weight: bold;
                color: #333;
            }}
        </style>
    </head>
    <body>
        <div class="box">
            <div class="ip">Ваш IP: {real_ip}</div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/favicon.ico')
def favicon():
    # Возвращаем "пустой" favicon, чтобы не было ошибки 404
    return '', 204

if __name__ == '__main__':
    app.run()