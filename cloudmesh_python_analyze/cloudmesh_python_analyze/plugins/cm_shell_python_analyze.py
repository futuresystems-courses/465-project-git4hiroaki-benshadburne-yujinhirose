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
              python_analyze deploy_pydoop NAME [--count=N] 
              python_analyze stop
              python_analyze do_analysis
              python_analyze visualize

          Arguments:

            NAME      Name of the clusters for Pydoop
            FILE      Name of the file to be downloaded

          Options:

             -v       verbose mode
             -f       specify the file 

          Example:

              python_analyze load -f [ABC file]

                     executes the python_analyze load command with the givenname

              python_analyze deploy_pydoop pydoop-cluster-ABC [--count=N] 

                      deploy the N virtual cluster for Pydoop along with Hadoop

        """
        # pprint(arguments)

        if arguments["NAME"] is None:
            Console.error("Please specify a host name")
        elif arguments['deploy_pydoop']:
          Console.ok("Start to deploy Pydoop")

          # Insert the argument into input for deploy_cluster
          name = arguments['NAME']

          # Deploy 3 virtual cluster using heat
          command_python_analyze.deploy_cluster(name) # see deploy_cluster in "command_python_analyze.py" 

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
