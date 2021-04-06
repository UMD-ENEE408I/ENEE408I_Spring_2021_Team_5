import os

File = "Levi.jpg"
os.chdir("/home/jszymkie/ENEE408I_Spring_2021_Team_5/Image")
os.system("git add " + File)
os.system("git commit --no-verify --allow-empty-message " + File)
#commit message still shows up :(
os.system("git push --set-upstream " + File + " master")
#This is untested because of commit
