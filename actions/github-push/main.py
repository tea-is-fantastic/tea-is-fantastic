import os, sys
import git

creds = sys.argv[1]
repo = sys.argv[2]
OUTPUT_PATH = sys.argv[3]
REPO_PATH = f"https://{creds}@github.com/{repo}"


if __name__ == '__main__':
    os.chdir(OUTPUT_PATH)
    os.system('git config --global user.email "tif@replyqa.com"')
    os.system('git config --global user.name "Abhinandan"')
    os.system("git init .")
    os.system("git add -A")
    os.system('git commit -am "woohoo"')
    os.system('git branch -M main')
    os.system(f'git remote add origin {REPO_PATH}')
    os.system("git push --all -f")
    # repo = git.Repo.init(OUTPUT_PATH)
    
    # for path, subdirs, files in os.walk(OUTPUT_PATH):
    #     for name in files:
    #         repo.index.add(os.path.join(path, name))

    # repo.index.commit("initial commit")
    # origin = repo.create_remote('origin', REPO_PATH)
    # # repo.create_head('master', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    # print("START")
    # origin.push(force=True, all=True).raise_if_error()
    # print("FINISH")

