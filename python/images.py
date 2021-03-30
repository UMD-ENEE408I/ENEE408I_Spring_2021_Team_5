from github import Github

g = Github("joeszym12@gmail.com", "#Lessthan7")

for repo in g.get_user().get_repos():
    print(repo.name)

# path = "/home/jszymkie/Desktop/PYPRO/images"
# name = "gil.jpg"
# image = path + "/" + name
# repo.create_file(git_file,"committing files", content, branch = "master")