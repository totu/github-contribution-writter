#!/usr/bin/env python3

import subprocess
import time

def create_commit(file_to_edit="dummy"):
    now = time.time()

    # Edit given file
    with open(file_to_edit, "a") as filu:
        filu.write(str(now) + "\n")

    # Create a commit
    cmd = f"git commit -am '{now}'"
    subprocess.call(cmd.split(" "))

    # Push to remote
    cmd = "git push"
    subprocess.call(cmd.split(" "))

if __name__ == "__main__":
    create_commit()
