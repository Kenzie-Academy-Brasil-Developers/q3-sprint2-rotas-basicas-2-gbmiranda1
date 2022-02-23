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
    format_time = now.strftime("%d") + "/"+ now.strftime("%m") + "/" + now.strftime("%Y") + " " + str(now)[11:19] + " " + now.strftime("%P").upper()
    msg = ""
    if int(now.strftime("%H")) > 18:
        msg = "Boa noite!"
    elif  18 >= int(now.strftime("%H")) >= 12:
        msg = "Boa tarde!"
    else:
        msg = "Bom dia!"
    return { "current_datetime": format_time, "message": msg }
    