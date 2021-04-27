import os

initial = os.getcwd()
print("Initial directory is:", initial)

path = initial + "/Image"
os.chdir(path)
print("New directory is:", path)

os.chdir(initial)
print("The original directory is:", initial)