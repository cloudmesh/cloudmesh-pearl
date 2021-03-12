Documentation
=============


[![image](https://img.shields.io/travis/TankerHQ/cloudmesh-pearl.svg?branch=main)](https://travis-ci.org/TankerHQ/cloudmesn-pearl)

[![image](https://img.shields.io/pypi/pyversions/cloudmesh-pearl.svg)](https://pypi.org/project/cloudmesh-pearl)

[![image](https://img.shields.io/pypi/v/cloudmesh-pearl.svg)](https://pypi.org/project/cloudmesh-pearl/)

[![image](https://img.shields.io/github/license/TankerHQ/python-cloudmesh-pearl.svg)](https://github.com/TankerHQ/python-cloudmesh-pearl/blob/main/LICENSE)

This command will help you to interact with perl from a remote machine easily.
The reason we wrote this program instead of using ssh directly is to focus on
the development of code on your local computer before you run them on perl.

To use the command you have to install it with pip in python3 virtualenv

If you do not have a venv you can create one on Linux with

```bash
$ python3 -m venv ~/ENV3
$ source ~/ENV3/bin/activate 
```

and on Windows with 

```bash
$ python -m venv ~/ENV3
$ source ~/ENV3/bin/activate 
```


```
module load Python/3.7.4-GCCcore-8.3.0
python --version
python -m venv ENV3
source ~/ENV3/bin/activate
pip install jupyterlab
pip install pip -U
pip install matplotlib
```

```
jupyter nbconvert --allow-errors --execute --to notebook  --output=Untitles-output.ipynb  Untitled.ipynb
```

```bash
echo "source ~/ENV3/bin/activate; which python" | ssh -i /home/green/.ssh/id_rsa.pub pearl063@ui.pearl.scd.stfc.ac.uk /bin/bash -l
```

```
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
export SYSTEMD_PAGER=

# User specific aliases and functions

source /etc/profile
module load Python/3.7.4-GCCcore-8.3.0

source ~/ENV3/bin/activate

PATH=$HOME/.local/bin:$HOME/bin:$PATH
```