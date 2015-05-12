export portalname=team-byh
export projectid=fg465b
export PORTALNAME=$portalname
export PROJECTID=projectid
export cloudmeshdir=./cloudmesh

curl https://raw.githubusercontent.com/cloudmesh/get/master/cloudmesh/ubuntu/14.04.sh | venv=$HOME/ENV bash
#git clone https://github.com/cloudmesh/cloudmesh.git

ssh-keygen -t rsa -C $PORTALNAME-ubuntu-vm-key
source $HOME/ENV/bin/activate
# ssh-keygen -t rsa -C $PORTALNAME-ubuntu-vm-key

eval `ssh-agent -s`
ssh-add

 cm-iu user fetch --username=$PORTALNAME
 cm-iu user create
 cd ~/cloudmesh

 # Setup fab
 fab india.configure
 fab mongo.reset
 fab server.start
