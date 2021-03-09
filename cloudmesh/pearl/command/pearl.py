from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.pearl.Pearl import Pearl

class PearlCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_pearl(self, args, arguments):
        """
        ::

          Usage:
                pearl user USER
                pearl queue
                pearl ssh
                pearl batch SCRIPT
                pearl run [--cpu=CPU] [--gpu=GPU]
                pearl sync to DIR
                pearl sync from
                pearl fuse DIR

          Interfaceing with pearl

          Arguments:
              USER     the username
              SCRIPT   script to be executed
              DIR      the DIRECTORY to be synced to pearl
              OPTIONS  options

        """

        pearl = Pearl()



        if arguments.user:

            pearl.user(arguments.USER)
            return

        try:
            pearl.check_user()
        except ValueError:
            Console.error("Please set the user with\n")
            Console.msg("   cms pearl user YOURUSERID\n")


        if arguments.queue:

            pearl.queue()

        elif arguments.ssh:

            pearl.ssh()

        elif arguments.run:

            pearl.run(cpu=arguments["--cpu"], gpu=arguments["--gpu"])
        """
            USER
                pearl batch SCRIPT
                pearl run [OPTIONS]
                pearl sync to DIR
                pearl sync from
                pearl fuse DIR
                pearl
        """

        return ""
