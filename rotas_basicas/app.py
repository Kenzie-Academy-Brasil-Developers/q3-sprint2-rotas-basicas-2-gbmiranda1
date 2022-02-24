# Seu código aqui
from flask import Flask
from datetime import datetime

app = Flask(__name__)
now = datetime.now()

@app.route('/')
def home():
    return {'data': 'Hello Flask!'}


@app.route('/current_datetime')
def current_datetime():
    format_time = now.strftime("%d/%m/%Y %H:%M:%S %p")
    msg = ""
    if int(now.strftime("%H")) > 18:
        msg = "Boa noite!"
    elif int(now.strftime("%H")) <= 18 and int(now.strftime("%H")) >= 12:
        msg = "Boa tarde!"
    else:
        msg = "Bom dia!"
    return { "current_datetime": format_time, "message": msg }
    