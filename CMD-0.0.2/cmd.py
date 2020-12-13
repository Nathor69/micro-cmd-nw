from math import *
import os
from data import *

class command:
  def cls():
    print("\n"*10)

  def boot():
    command.cls()
    print("""\n
     _____ __  __ _____     ___   ___   ___  
    / ____|  \/  |  __ \   / _ \ / _ \ |__ \ 
   | |    | \  / | |  | | | | | | | | |   ) |
   | |    | |\/| | |  | | | | | | | | |  / / 
   | |____| |  | | |__| | | |_| | |_| | / /_ 
    \_____|_|  |_|_____/   \___(_)___(_)____|
    \n""")
    login()

  def dir():
    ldir=os.listdir()
    for i in ldir:
      print(i)

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
    if err==2:
      print("Cannot remove root user")
    if err==3:
      print("Command not found")

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
        with open("data.py","w") as loginsfile:
          logins.append((nlog,npwd))
          loginsfile.seek(1)
          loginsfile.write("logins="+str(logins))

  def remlog():
    if isroot==False:
      error(1)
    else:
      rlog=input("remove user: ")
      if rlog=='root':
        error(2)
        return
      alrexst=0
      for i in logins:
        if i[0]==rlog:
          alrexst+=1
      if alrexst==0:
        print("\nThis account does not exist")
        print("Sorry dude\n")
      else:
        conf=input("R u sure? (y/n)")
        if conf!="y":
          return
        with open("data.py","w") as loginsfile:
          for i in logins:
            if i[0]==rlog:
              logins.remove(i)
          loginsfile.truncate(0)
          loginsfile.seek(1)
          loginsfile.write("logins="+str(logins))

def login():
  global clog
  clog=input("user: ")
  cpwd=input("pswd: ")
  if logins.count((clog,cpwd))==1:
    print("")
    if clog=="root":
      global isroot
      isroot=True
      print("You\'re connected as root")
    else:
      isroot=False
    print("yay\n")
  else:
    print("\nThis account does not exist")
    print("u stoopid just try again\n")
    login()

def commandinput():
  global cinput
  cinput=input("nw@"+str(clog)+":~$ ")
  cinput=cinput.split()
  runapp(cinput[0])

def runapp(commandtext):
  if commandtext=='dir':
    command.dir()
  if commandtext=='addlog':
    command.addlog()
  if commandtext=='remlog':
    command.remlog()
  if commandtext=='rdfl':
    command.rdfl(cinput[1])
  if commandtext=='cls':
    command.cls()
  else:
    command.error(3)

command.boot()
while True:
  commandinput()
