import MySQLdb
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<br><h1 style='color:blue'>Hello There! My app is coming!</h1>"

@application.route("/login")
def login():
    return "<h1>Login page</h1>"

@application.route("/song")
def song():
    return application.send_static_file('Saiyaan.mp3')

if __name__ == "__main__":
    application.run(host='0.0.0.0')
