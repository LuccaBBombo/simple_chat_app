import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Main page with instructions on how to send a message"""
    return "To send a message use /USERNAME/MESSAGE"

@app.route('/<username>')
def user(username):
    """Page that greets the user, displaying their chosen username"""
    return "Hi " + username

@app.route('/<username>/<message>')
def send_message (username, message):
     """Page that displays the username and message"""
    return "{0}: {1}".format(username, message)


app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
