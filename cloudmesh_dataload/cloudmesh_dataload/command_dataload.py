from cloudmesh_base.Shell import Shell
import os

class command_dataload(object):

    @classmethod
    def status(cls, host):
        msg = "Unknown host"
        try:
            msg = Shell.ping("-c", "1", host)
        except:
            pass
        if "1 packets transmitted, 1 packets received" in msg:
            return True
        elif "Unknown host" in msg:
            return False
        else:
            return False

    @classmethod
    def dataload(cls, src_url="http://stat-computing.org/dataexpo/2009/2007.csv.bz2"):
        print("Downloading the data source ugins wget")

        # Download the data from provided URL site
        os.system("wget " + src_url)
        return 1













