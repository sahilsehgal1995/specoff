import MySQLdb
from flask.ext.cors import CORS
from flask import Flask, request, session
from userdatabase import userLogin, userRegister

application = Flask(__name__)
CORS(application)

@application.route("/", methods=['GET', 'POST'])
def hello():
    return "<br><h1 style='color:blue'>Hello There! My app is coming!</h1>"

@application.route('/login/', methods=['GET', 'POST'])
def login():
  error=''
  try:
    if request.method =='POST':
      reply = userLogin("users", request.form['username'], request.form['password'])
      if reply is True:
	session['logged_in'] = True
	session['username'] = request.form['username']
	return "Successfull login"
    
    return "Authentication failed"
  
  except Exception as e:
    return (str(e))

@application.route('/userregister/', methods=['GET', 'POST'])
def adminRegisteration():
  try:
    if request.method == 'POST':
      reply = userRegister('users', request.form['name'], request.form['emailid'], request.form['password'])
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
