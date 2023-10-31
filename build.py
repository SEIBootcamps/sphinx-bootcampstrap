"""Compile CSS and other assets to include in dist."""

import subprocess


def build():
    try:
        subprocess.run(["yarn", "run", "build"], capture_output=True, check=True)
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode("utf-8"))
        raise e


if __name__ == "__main__":
    build()
