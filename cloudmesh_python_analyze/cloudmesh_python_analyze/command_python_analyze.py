from cloudmesh_base.Shell import Shell


class command_python_analyze(object):

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
    def deploy_cluster(cls, name):

        print("Setting up virtual clusters and install Hadoop")

        # Start ssh-agent and resgister the RSA keys
        os.system("eval $(ssh-agent -s)")
        os.system("ssh-add ~/.ssh/id_rsa")



        # Run heat command to create virtual clusters
        # os.system("heat stack-create -u https://raw.githubusercontent.com/futuresystems/465-project-git4hiroaki-benshadburne-yujinhirose/master/hadoop-cluster-airline-del-pred.yaml -P "KeyName=hshioi-india-key;PublicKeyString=`cat ~/.ssh/id_rsa.pub`;PrivateKeyString=`cat ~/.ssh/id_rsa`" heat-hadoop-cluster-$PORTALNAME")
        # os.system("heat stack-create -u https://raw.githubusercontent.com/futuresystems/465-project-git4hiroaki-benshadburne-yujinhirose/5eaa96873642d7b7499cc04a77cf6ca2d5af9f7d/hadoop-cluster-airline-del-pred.yaml -P "KeyName=hshioi-india-key;PublicKeyString=`cat ~/.ssh/id_rsa.pub`;PrivateKeyString=`cat ~/.ssh/id_rsa`" heat-hadoop-cluster-$PORTALNAME")
        os.system('heat stack-create -u https://raw.githubusercontent.com/futuresystems/465-project-git4hiroaki-benshadburne-yujinhirose/masd_rsa.pub`;PrivateKeyString=`cat ~/.ssh/id_rsa`;Hadoop1Name='';Hadoop2Name='';Hadoop3Name=''" heat-hadoop-cluster-cm')

        # If user input the location of public/private key
        # name = arguments['NAME'] # Arbitrary name e.g., heat-hadoop-cluster-hshioi0620'
        # public_key = arguments['--public_key'] # ~/.ssh/id_rsa.pub
        # private_key = arguments['--private_key'] # ~/.ssh/id_rsa
        # key_name = arguments['--key_name'] # should be resgistered in OpenStack
        # os.system('heat stack-create -u https://raw.githubusercontent.com/futuresystems/465-project-git4hiroaki-benshadburne-yujinhirose/master/hadoop-cluster-airline-del-pred.yaml -P "KeyName=' + key_name +';PublicKeyString=`cat ' + public_key + '`;PrivateKeyString=`cat ' + private_key + '` ' + name)

        # # Run cm launcher command to create hadoop clusters
        # os.system('cm launcher pydoop-cluster-airline')

        return 1











