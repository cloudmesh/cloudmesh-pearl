from cloudmesh.common.variables import Variables
import os
from cloudmesh.common.util import path_expand
from cloudmesh.common.console import Console

class Pearl(object):

    def __init__(self):

        self.variables = Variables()
        self.host = "ui.pearl.scd.stfc.ac.uk"
        try:
            self.username = self.variables["pearl.username"]
        except:
            Console.error("Username not set")
        try:
            self.key = self.variables["pearl.key"]
        except:
            Console.error("Key not set")
        try:
            self.verbose = self.variables["pearl.verbose"]
        except:
            self.variables["pearl.verbose"] = self.verbose = False


    def check_user(self):
        if self.username is None:
            raise ValueError("Your user name for perl is not set")

    def _execute(self, command):
        command = f"ssh -i {self.key} {self.username}@{self.host} '{command}'"
        if self.verbose:
            print (command)
        os.system(command)

    def set_verbose(self, on=None):
        if on is None or on:
            self.variables["pearl.verbose"] = True
        else:
            self.variables["pearl.verbose"] = on.lower() in ["1", "true", "on"]
        if self.variables["pearl.verbose"]:
            os.system("cms debug on")
        else:
            os.system("cms debug off")

    def set_user(self, username):
        if "@" in username:
            username = username.split("@")[0]
        self.username = self.variables["pearl.username"] = username

    def set_key(self, key):
        self.key = path_expand(key)
        self.variables["pearl.key"] = self.key

    def queue(self):
        self._execute("squeue")

    def ssh(self, execute=None):
        if execute is not None:
            execute = f'"{execute}"'
        else:
            execute = ""
        command = f"ssh -i {self.key} {self.username}@{self.host} {execute}"
        if self.verbose:
            print (command)
        os.system(command)

    def batch(self, SCRIPT):
        pass

    def run(self, cpu=None, gpu=None):
        gpu = gpu or 1
        cpu = cpu or 1
        command = f"srun -n {cpu} --gres=gpu:{gpu} --pty /bin/bash"
        srun = f"ssh -i {self.key} -t {self.username}@{self.host} '{command}'"
        os.system(srun)

    def ls(self, directory):
        self.ssh(f"ls -lisa {directory}")

    def sync_put(self, directory):
        command = f"rsync -i {self.key} -r {directory} {self.username}@{self.host}:{directory}"
        if self.verbose:
            print (command)
        os.system(command)
        self.ls(directory)

    def sync_get(self, directory):
        command = f"rsync -i {self.key} -r {self.username}@{self.host}:{directory} {directory}"
        if self.verbose:
            print (command)
        os.system(command)
        os.system(f"ls -lisa {directory}")

    def fuse(self, DIR):
        pass

    def info(self):
        print()
        print("Username:", self.username)
        print("Key:     ", self.key)
        print("Verbose: ", self.verbose)
        print()
