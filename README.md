# Micro "cmd" on NW
A tiny "cmd" in the NumWorks Python app (on [Omega](https://getomega.dev))  
(just to test some function)  
(not complete at all)  
Ver 0.1.2
  
| Command             | What that does                    |
|----------------------|-----------------------------------|
| `dir`                | Display filenames                 |
| `rdfl filename`     | Read a file                       |
| `addlog`             | Add a user                        |
| `remlog`             | Remove a user                     |
| `cls`                | Print some blank lines            |
| `mkfile filename`                | Create a file            |
| `rename src dst`                | Rename a file            |
| `rm src`                | Remove a file            |
| `cp src dst`                | Duplicate a file            |
| `sysinfo`                | Infos about the system            |
| `pwegn`               | Password generator      |
| `echo`                | Display/Write something |
| `help`                  | List of the commands    |
| `pwd`                     | Show directory path     |
| `exit`                | Exit the CMD            |
| others are coming... | (°u°)                             |
  
Root user is `root` and pswd `hey`  
Change in `data.py` if you want  
If running on pc, set `numworks` to `0` or `1` if running on NumWorks  
Please set your Python text size to small so the logo will print correctly (on NumWorks)

Ideas:
- TUI (don't know if that will be smooth on NW)
- option to add other root users
- encrypt passwords
- change passwords
- Unix-like command names
- more software and stuff:
  - write in file
  - agenda
  - etc...
- installer script
  - choose between NW and PC version
  - change root name and password
  - etc...
- change database management (use a single variable for all data or use json/other)
- etc...
