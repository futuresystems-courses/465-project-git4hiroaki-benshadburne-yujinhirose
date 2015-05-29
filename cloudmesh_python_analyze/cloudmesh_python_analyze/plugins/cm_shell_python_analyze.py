from __future__ import print_function
import os
from cmd3.console import Console
from cmd3.shell import command

from cloudmesh_python_analyze.command_python_analyze import command_python_analyze


class cm_shell_python_analyze:

    def activate_cm_shell_python_analyze(self):
        self.register_command_topic('mycommands', 'python_analyze')

    @command
    def do_python_analyze(self, args, arguments):
        """
        ::

          Usage:
              python_analyze load -f FILE
              python_analyze deploy
              python_analyze stop
              python_analyze do_analysis
              python_analyze visualize

          tests via ping if the host ith the give NAME is reachable

          Arguments:

            NAME      Name of the machine to test
            FILE      Name of the file to be loaded

          Options:

             -v       verbose mode
             -f       specify the file

          Example:

               python_analyze load -f [ABC file]

                     executes the python_analyze load command with the givenname






        """
        # pprint(arguments)

        if arguments["NAME"] is None:
            Console.error("Please specify a host name")
        else:
            host = arguments["NAME"]
            Console.info("trying to reach {0}".format(host))
            status = command_python_analyze.status(host)
            if status:
                Console.info("machine " + host + " has been found. ok.")
            else:
                Console.error("machine " + host + " not reachable. error.")
        pass

if __name__ == '__main__':
    command = cm_shell_python_analyze()
    command.do_python_analyze("iu.edu")
    command.do_python_analyze("iu.edu-wrong")
