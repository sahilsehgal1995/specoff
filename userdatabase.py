import MySQLdb
from MySQLdb import escape_string as thwart
from passlib.hash import sha256_crypt
import gc
import os

def connection():
  conn =MySQLdb.connect(host='localhost', user='root', passwd='faceitoff', db='users')
  c = conn.cursor()
  return c, conn

def userLogin(databaseName, username, password):
  try:
    c,conn = connection()
    databaseName = databaseName.replace(" ","")
    c.execute("use %s ;" %databaseName)
    conn.commit()
    if c.execute("select * from users where username= '%s'" %(thwart(username))):
	  data = c.execute("select * from users where username= '%s'" %(thwart(username)))
	  data = c.fetchone()[1]
	  if sha256_crypt.verify(password,data):
	    return True
	  else:
	    return False
    else:
      return False
  except Exception as e:
    return str(e)

def userRegister(databaseName, name, email, password):
  try:
    c,conn = connection()
    databaseName = databaseName.replace(" ","")
    c.execute("use %s ;" %databaseName)
    conn.commit()
    x = c.execute("select * from users where username = '%s'" %(thwart(email)))
      if int(x) > 0:
	return "User already exists"

      else:
	c.execute("INSERT INTO user (name, email, password) values ('%s','%s','%s')" %(thwart(name),thwart(email),sha256_crypt.encrypt(str(thwart(password))))
	conn.commit()
	c.close()
	conn.close()
	gc.collect()
	return "User Registered"

  except Exception as e:
    return str(e)