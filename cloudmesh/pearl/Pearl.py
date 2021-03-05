from cloudmesh.common.variables import Variables
import os

class Pearl(object):

    def __init__(self):
        print ("init")
        self.variables = Variables()
        self.host = "ui.pearl.scd.stfc.ac.uk"
        try:
            self.username = self.variables["pearl_username"]
        except:
            self.username = None

    def _execute(self, command):
        command = f"ssh {self.username}@{self.host} '{command}'"
        print (command)
        os.system(command)

    def user(self, username):
        self.username = self.variables["pearl_username"] = username

    def queue(self):
        self._execute("squeue")

    def ssh(self):
        command = f"ssh {self.username}@{self.host}"
        print (command)
        os.system(command)

    def batch(self, SCRIPT):
        pass

    def run(self, **kwargs):
        # OPTIONS
        pass

    def sync_to(self, DIR):
        pass

    def sync_from(self):
        pass

    def fuse(self, DIR):
        pass

