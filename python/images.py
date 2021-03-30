from github import Github

g = Github("Token")
for repo in g.get_user().get_repos():
    print(repo.name)
