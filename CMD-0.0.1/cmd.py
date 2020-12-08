from math import *
from os import *
from data import *

isroot = False

def boot():
  print("\nCMD 0.0.1\n")
  login()

def login():
  clog=input("user: ")
  cpwd=input("pswd: ")
  if logins.count((clog,cpwd))==1:
    print("")
    if clog=="root":
      global isroot
      isroot=True
      print("You\'re connected as root")
    print("yay\n")
  else:
    print("\nThis account does not exist")
    print("u stoopid just try again\n")
    login()

def dir():
  ldir=listdir()
  print("")
  for i in ldir:
    print(ldir[i])
  print("")

def rdfl(fl):
  file=open(fl)
  file.seek(1)
  print("###START OF "+fl+"###")
  print(file.read(1000000000))
  print("####END OF "+fl+"####")
  file.close
  
def error(err):
  if err==1:
    print("You are not connected as root")
    print("Error: permission denied")

def addlog():  
  if isroot==False:
    error(1)
  else:
    nlog=input("new user: ")
    npwd=input("new pswd: ")
    alrexst=0
    for i in logins:
      if logins[i][0]==nlog:
        alrexst+=1
    if alrexst>0:
      print("\nThis account already exist")
      print("Sorry dude\n")
    else:
      loginsfile=open("data.py","w")
      logins.append((nlog,npwd))
      loginsfile.seek(9)
      loginsfile.write(str(logins))
      
boot()
