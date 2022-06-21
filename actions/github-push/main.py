import os, sys
import git

creds = sys.argv[1]
repo = sys.argv[2]
OUTPUT_PATH = sys.argv[3]
REPO_PATH = f"https://{creds}@github.com/{repo}"


if __name__ == '__main__':
    repo = git.Repo.init(OUTPUT_PATH)
    
    for path, subdirs, files in os.walk(OUTPUT_PATH):
        for name in files:
            repo.index.add(os.path.join(path, name))

    repo.index.commit("initial commit")
    origin = repo.create_remote('origin', REPO_PATH)
    print(REPO_PATH)
    print([r for r in origin.refs])
    repo.create_head('master', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.push()

