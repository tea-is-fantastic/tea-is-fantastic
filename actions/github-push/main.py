import base64, sys
from github import Github, InputGitTreeElement


token = sys.argv[1]
reposit = sys.argv[2]
folder = sys.argv[3]

g = Github(token)
repo = g.get_user().get_repo(reposit)  # repo name

file_list = []
file_names = []

for path, subdirs, files in os.walk(folder):
    for name in files:
        file_list.append(os.path.join(path, name))
        file_names.append(name)

commit_message = 'python commit'
master_ref = repo.get_git_ref('heads/main')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)

element_list = list()
for i, entry in enumerate(file_list):
    with open(entry) as input_file:
        data = input_file.read()
    if entry.endswith('.png'):  # images must be encoded
        data = base64.b64encode(data)
    element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
    element_list.append(element)

tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)
