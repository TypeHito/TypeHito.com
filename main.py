from flask import Flask, render_template, request, url_for, flash, redirect
from microservice.telegram_bot.bot_answer import send_message
from microservice.telegram_bot.bot_configs import owner
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello from Typehito'

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]


@app.route('/send')
def send():
    return render_template('send.html')


@app.route('/')
def index():
    print(request.args)
    # if request.method == 'POST':
    if request.args:
        name = request.args['name']
        email = request.args['email']
        subject = request.args['subject']
        msg = request.args['msg_text']
        send_message(owner, f"Name: {name}'\n email: {email}\n subject:{subject}\nMessage: {msg}")
        redirect("127.0.0.1:5000/send")
    return render_template('index.html')

app.run()