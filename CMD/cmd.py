try :
  import os
except:
  print("Please use Omega")
try:
  from data import *
except:
  print("Data file not found")

#PC and NumWorks compatibility
#0 is false, 1 is true
numworks = 0

class command:
  def cls():
    print("\n"*14)
  def boot():
    print("""\n
   _____ __  __ _____     ___  __   ___  
  / ____|  \/  |  __ \   / _ \/_ | |__ \ 
 | |    | \  / | |  | | | | | || |    ) |
 | |    | |\/| | |  | | | | | || |   / / 
 | |____| |  | | |__| | | |_| || |_ / /_ 
  \_____|_|  |_|_____/   \___(_)_(_)____|
    \n""")
    sysinfo=os.uname()
    #For NW and PC compatibility
    try:
      for i in range(len(sysinfo)):
        print(sysinfo[i])
      print("")
    except:
      for i in sysinfo:
        print(sysinfo[i])
      print("")
    login()
  def echo():
      echo1  = input("echo ")
      print(echo1)
  def dir():
    ldir=os.listdir()
    for i in ldir:
      print(i)
  def rdfl(fl):
    with open(fl) as file:
      file.seek(numworks)
      print("###START OF "+fl+"###")
      print(file.read())
      print("####END OF "+fl+"####")
  def help():
    print("""
dir                 | Display filenames
pwgen               | Password generator
cls                 | Display the directory
rdfl filename       | Read a file
addlog              | Add a user
remlog              | Remove a user
cls                 | Print some blank lines
mkfile filename     | Create a file
rename src dst      | Rename a file
rm src              | Remove a file
cp src dst          | Duplicate a file
""")
    help1 = input("More commands? Y//N ")
    if help1=='Y':
        print("""
sysinfo             | Infos about the system
pwd                 | Show directory path
exit                | Exit the CMD
echo                | Display/Write something
help                | List of the commands
others are coming...| (°u°)
""")
    else:
        pass

  def error(err):
    if err==1:
      print("You are not connected as root")
      print("Error: permission denied")
    if err==2:
      print("Cannot remove root user")
    if err==3:
      print("Command not found")
    if err==4:
      print("File not found")
  def pwd():
   print("C:\\")
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
          loginsfile.seek(numworks)
          loginsfile.write("logins="+str(logins))
  def telnetstarwars():
      print("""\n
      _                                      
  ___| |_ __ _ _ __  
 / __| __/ _` | '__| 
 \__ \ || (_| | |   
 |___/\__\__,_|_|    
__      ____ _ _ __ ___ 
\ \ /\ / / _` | '__/ __|
 \ V  V / (_| | |  \__ \\
  \_/\_/ \____|_|  |___/

\n""")
  def pwgen():
    from random import *
    import time
    caractère = ("""ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]
    ^_`{|}~""").lower()
    a = int(input("Number of characters in the password: "))
    print("The password is:")
    for i in range(a):
      password = ""
      cara = choice(caractère)
      print(cara, end = '')
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
          loginsfile.seek(numworks)
          loginsfile.write("logins="+str(logins))

  def renamefile(src,dst):
    try:
      os.rename(src,dst)
      print(src,"renamed to",dst)
    except:
      command.error(4)

  def createfile(dst):
    try:
      open(dst,"w").close()
      print(dst,"created")
    except:
      command.error(4)

  def removefile(src):
    try:
      os.remove(src)
      print(src,"removed")
    except:
      command.error(4)

  def cpfile(src, dst):
    try:
      with open(src) as file:
        nfile=open(dst,"w")
        nfile.write(file.read())
        nfile.close()
        print("Duplicated",src,"into",dst)
    except:
      command.error(4)

  def sysinfo():
    sysinfo=os.uname()
    #For NW and PC compatibility
    try:
      for i in range(len(sysinfo)):
        print(sysinfo[i])
    except:
      for i in sysinfo:
        print(sysinfo[i])

  def changepswd(user):
    if isroot==False:
      error(1)
    alrexst=0
    for i in logins:
      if i[0]==rlog:
        alrexst+=1
    if alrexst==0:
      print("\nThis account does not exist")
      print("Sorry dude\n")
    npswd=input("New password: ")
      #TODO: finish this


def login():
  global clog
  global isroot
  clog=input("user: ")
  cpwd=input("pswd: ")
  if logins.count((clog,cpwd))==1:
    print("")
    if clog=="root":
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
  elif commandtext=='addlog':
    command.addlog()
  elif commandtext=='remlog':
    command.remlog()
  elif commandtext=='rdfl':
    try:
      command.rdfl(cinput[1])
    except:
      command.error(4)
  elif commandtext=='cls':
    command.cls()
  elif commandtext=='exit':
    global exit
    exit=True
  elif commandtext=='rename':
    command.renamefile(cinput[1],cinput[2])
  elif commandtext=='mkfile':
    command.createfile(cinput[1])
  elif commandtext=='rm':
    command.removefile(cinput[1])
  elif commandtext=='cp':
    command.cpfile(cinput[1],cinput[2])
  elif commandtext=='sysinfo':
    command.sysinfo()
  elif commandtext=='help':
    command.help()
  elif commandtext=='pwd':
    command.pwd()
  elif commandtext=='pwgen':
    command.pwgen()
    print('\n')
  elif commandtext=='Telnetstarwars':
      command.telnetstarwars()
  elif commandtext=='echo':
      command.echo()
  else:
    command.error(3)

command.boot()
global exit
exit=False
while True:
  try:
    commandinput()
    if exit:
      break
  except:
    print("Error, please try again")
