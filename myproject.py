import MySQLdb
from flask.ext.cors import CORS
from flask import Flask, request, session, jsonify
from userdatabase import userLogin, userRegister

application = Flask(__name__)
CORS(application)
application.config['SECRET_KEY'] = 'HARD TO GUESS'

@application.route("/", methods=['GET', 'POST'])
def hello():
    return "<br><h1 style='color:blue'>Hello There! My app is coming!</h1>"

@application.route('/login/', methods=['GET', 'POST'])
def login():
  try:
    if request.method =='POST':
      reply = userLogin("users", request.args.get('email'), request.args.get('password'))
      if reply is True:
	return "Successfull login"
      else:
	return "Authentication failed"
    
    return "Unable to process"
  
  except Exception as e:
    return (str(e))

@application.route('/userregister/', methods=['GET', 'POST'])
def adminRegisteration():
  try:
    if request.method == 'POST':
      reply = userRegister('users', request.args.get('name'), request.args.get('email'), request.args.get('password'))
      return reply
    
    else:
      return "Unable to register"
    
  except Exception as e:
    return str(e)

@application.route("/song")
def song():
    return application.send_static_file('Saiyaan.mp3')

if __name__ == "__main__":
    application.run(host='0.0.0.0')
