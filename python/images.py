import os

File = "(file name)"
os.chdir("/home/(username)/ENEE408I_Spring_2021_Team_5")
os.system("git status")
os.system("git add Image/" + File)
os.system("git status")
os.system("git commit -m image")
os.system("git push")
os.system("git push")