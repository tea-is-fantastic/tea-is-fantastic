import os, sys
import git

REPO_PATH = sys.argv[1]
OUTPUT_PATH = sys.argv[2]


if __name__ == '__main__':
    repo = git.Repo.init(OUTPUT_PATH)
    
    for path, subdirs, files in os.walk(OUTPUT_PATH):
        for name in files:
            repo.index.add(os.path.join(path, name))

    repo.index.commit("initial commit")
    origin = repo.create_remote('origin', REPO_PATH)
    repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    origin.push()

