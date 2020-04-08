#!/usr/bin/env python
import subprocess
import sys

conda_env_creation = True if "{{ cookiecutter.create_conda_env }}" == "Yes" else False
data_version_control = True if "{{ cookiecutter.DVC_setting }}" == "Yes" else False


if conda_env_creation:
    try:
        subprocess.run(["make", "init_environment"], check=True)
    except subprocess.CalledProcessError:
        sys.exit(1)



if data_version_control:
    try:
        subprocess.run(["make", "init_dvc"], check=True)
    except subprocess.CalledProcessError:
        sys.exit(1)
