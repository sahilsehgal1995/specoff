import MySQLdb
from MySQLdb import escape_string as thwart
from passlib.hash import sha256_crypt
import gc
import timeit
import os
import json
import random
import resource
import time

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
    if c.execute("select * from user where email= '%s'" %(thwart(username))):
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
  
def loop():
  L = []
  for i in range(100000):
    L.append(i)
  return (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)

def nestedloop():
  L = []
  for i in range(100):
    for j in range(100):
      L.append(i)
  return (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)

def fib():
 n = 10000
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)

def bruteforce():
  L1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  L2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  L3=['0','1','2','3','4','5','6','7','8','9']
  L4=L1+L2+L3
  user='abcd'
  sum=""
  for i in range(0,len(L4)-2):
    sum=L4[i]+L4[i+1]
    if sum==user:
      break;
  return (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)

def matmul():
  # 3x3 matrix
  X = [[12,7,3],
      [4 ,5,6],
      [7 ,8,9]]
  # 3x4 matrix
  Y = [[5,8,1,2],
      [6,7,3,0],
      [4,5,9,1]]
  # result is 3x4
  result = [[0,0,0,0],
	  [0,0,0,0],
	  [0,0,0,0]]
  # iterate through rows of X
  for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
      # iterate through rows of Y
      for k in range(len(Y)):
	  result[i][j] += X[i][k] * Y[k][j]
  return (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)
ET = dict()

def testing(progname):
  if(progname == 'Loop'):
    start = time.clock()
    memory = loop()
    end = time.clock()
    ET['start'] = start
    ET['end'] = end
    #ET['Memory'] = memory
    return str(json.dumps(ET))
  
  elif(progname == 'Nested loop'):
    start = time.clock()
    memory = nestedloop()
    end = time.clock()
    ET['start'] = start
    ET['end'] = end
    #ET['Memory'] = memory
    return str(json.dumps(ET))
  
  elif(progname == 'fibonacci series'):
    start = time.clock()
    memory = fib()
    end = time.clock()
    ET['start'] = start
    ET['end'] = end
    #ET['Memory'] = memory
    return str(json.dumps(ET))

  elif(progname == 'Brute force'):
    start = time.clock()
    memory = bruteforce()
    end = time.clock()
    ET['start'] = start
    ET['end'] = end
    #ET['Memory'] = memory
    return str(json.dumps(ET))
  
  elif(progname == 'matrix multiplication'):
    start = time.clock()
    memory = matmul()
    end = time.clock()
    ET['start'] = start
    ET['end'] = end
    #ET['Memory'] = memory
    return str(json.dumps(ET)) 
  return str(json.dumps(ET))

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
      c.execute("INSERT INTO user (name, email, password) values ('%s','%s','%s')" %(thwart(name),thwart(email),sha256_crypt.encrypt(str(thwart(password)))))
      conn.commit()
      c.close()
      conn.close()
      gc.collect()
      return "Registeration done Successfully"

  except Exception as e:
    return str(e)
  
if __name__ == '__main__':
  print testing('Loop')
  print testing('Nested loop')
  print testing('fibonacci series')
  print testing('Brute force')
  print testing('matrix multiplication')
  print testing('matrix multiplicatiossssn')