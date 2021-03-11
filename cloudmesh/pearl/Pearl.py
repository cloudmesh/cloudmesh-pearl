from cloudmesh.common.variables import Variables
import os

class Pearl(object):

    def __init__(self):
        self.variables = Variables()
        self.host = "ui.pearl.scd.stfc.ac.uk"
        try:
            self.username = self.variables["pearl_username"]
        except:
            self.username = None

    def check_user(self):
        if self.username is None:
            raise ValueError("Your user name for perl is not set")

    def _execute(self, command):
        command = f"ssh {self.username}@{self.host} '{command}'"
        print (command)
        os.system(command)

    def set_user(self, username):
        if "@" in username:
            username = username.split("@")[0]
        self.username = self.variables["pearl_username"] = username

    def queue(self):
        self._execute("squeue")

    def ssh(self, execute=None):
        if execute is not None:
            execute = f'"{execute}"'
        else:
            execute = ""
        command = f"ssh {self.username}@{self.host} {execute}"
        print (command)
        os.system(command)

    def batch(self, SCRIPT):
        pass

    def run(self, cpu=None, gpu=None):
        gpu = gpu or 1
        cpu = cpu or 1
        command = f"srun -n {cpu} --gres=gpu:{gpu} --pty /bin/bash"
        srun = f"ssh -t {self.username}@{self.host} '{command}'"
        os.system(srun)

    def ls(self, directory):
        self.ssh(f"ls -lisa {directory}")

    def sync_put(self, directory):
        command = f"rsync -r {directory} {self.username}@{self.host}:{directory}"
        print (command)
        os.system(command)
        self.ls(directory)

    def sync_get(self, directory):
        command = f"rsync -r {self.username}@{self.host}:{directory} {directory}"
        print (command)
        os.system(command)
        os.system(f"ls -lisa {directory}")

    def fuse(self, DIR):
        pass

