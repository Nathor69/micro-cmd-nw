from math import *
import os
from data import *

isroot = False

def boot():
  print("""\n
   _____ __  __ _____     ___   ___  __ 
  / ____|  \/  |  __ \   / _ \ / _ \/_ |
 | |    | \  / | |  | | | | | | | | || |
 | |    | |\/| | |  | | | | | | | | || |
 | |____| |  | | |__| | | |_| | |_| || |
  \_____|_|  |_|_____/   \___(_)___(_)_|
  \n""")
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
    print(i)
  print("")

def rdfl(fl):
  file=open(fl)
  file.seek(1)
  print("###START OF "+fl+"###")
  print(file.read())
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
      if i[0]==nlog:
        alrexst+=1
    if alrexst>0:
      print("\nThis account already exist")
      print("Sorry dude\n")
    else:
      loginsfile=open("data.py","w")
      logins.append((nlog,npwd))
      loginsfile.write("logins="+str(logins))
      loginsfile.close()
      
boot()
