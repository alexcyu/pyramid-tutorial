import os
import subprocess

cwd = os.getcwd()
#export VENV=~/projects/quick_tutorial/env
# export VENV=~/projects/tutorials/pyramid/quick_tutorial/debugtoolbar/env
# $VENV/bin/pip install pyramid==2.0.1 waitress
os.system('cmd cwd  "python3 -m venv $VENV"')
os.system('"$VENV/bin/pip install "pyramid==2.0.1" waitress"')

#subprocess.run(["python3 -m venv $VENV"])
#subprocess.run(['$VENV/bin/pip install "pyramid==2.0.1" waitress'])
