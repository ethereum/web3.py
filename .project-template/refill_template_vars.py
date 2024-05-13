#!/usr/bin/env python3

import os
import sys
from pathlib import Path
import subprocess


def main():
    template_dir = Path(os.path.dirname(sys.argv[0]))
    template_vars_file = template_dir / "template_vars.txt"
    fill_template_vars_script = template_dir / "fill_template_vars.py"

    with open(template_vars_file, "r") as input_file:
        content_lines = input_file.readlines()

    process = subprocess.Popen(
        [sys.executable, str(fill_template_vars_script)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    for line in content_lines:
        process.stdin.write(line)
        process.stdin.flush()

    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Error occurred: {stderr}")
        sys.exit(1)

    print(stdout)


if __name__ == "__main__":
    main()
