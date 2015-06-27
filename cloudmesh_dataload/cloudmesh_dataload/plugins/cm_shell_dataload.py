from __future__ import print_function
import os
from cmd3.console import Console
from cmd3.shell import command
import subprocess
import pprint

# Refer to our original commands
from cloudmesh_dataload.command_dataload import command_dataload

class cm_shell_dataload:

    def activate_cm_shell_dataload(self):
        self.register_command_topic('mycommands', 'dataload')

    @command
    def do_dataload(self, args, arguments):
        """
        ::
          Usage:
	            dataload start --url=U
	            dataload delete NAME

          Arguments:
            NAME      Name of the downloaded file to be deleted

          Options:
	           --url=U   Data source of URL

        """
        if arguments['start']:
            Console.ok("Starting to download the data source from your specified URL")
            Console.ok("[Default url is: http://stat-computing.org/dataexpo/2009/2007.csv.bz2]")
            str_url = arguments['--url'] or "http://stat-computing.org/dataexpo/2009/2007.csv.bz2"

            # Download the file 
            command_dataload.dataload(str_url)

        elif arguments['delete']:
            Console.ok("Deleting downloaded source data")
            delete_file = arguments['Filename']
            command_dataload.delete(delete_file)
        else:
            Console.error("Invalid dataload command. Please see 'cm dataload'")
        pass

if __name__ == '__main__':
    command = cm_shell_dataload()
    command.do_dataload("iu.edu")
    command.do_dataload("iu.edu-wrong")






# pprint(arguments)
# elif arguments["start"]:
# if arguments['start']:
#   Console.ok('Start to download the data from specified URL')
#   Console.ok('Done by Hiroaki')
#   str_url = arguments['--url']    
    #subprocess.call(["wget ", str_url])
#   subprocess.call("ls")
#   subprocess.call("wget https://github.com/futuresystems/465-project-datawarehousemining/tree/master/cloudmesh_wikicount")
#   subprocess.call("cd ..")
