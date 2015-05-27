
# This script is created for deploying the analysis environment for 
airline delay detection
# - Refence -  
# 
# Predicting Airline Delays with Hadoop
# 
http://cloudmesh.github.io/introduction_to_cloud_computing/projects/sample_project_airline_delays.html
# 
# Data Science with Hadoop - predicting airline delays - part 1
# 
http://nbviewer.ipython.org/github/ofermend/IPython-notebooks/blob/master/blog-part-1.ipynb

# Procedures
# 1 Cloudmesh instllation
# 2 Run cm launcher hadoop, which create 1 master and 3 slave 
virtual cluster
# 3 



# =====================================================
echo '--- Set up VM from scratch --- Process (1)' 
# =====================================================

###### On Futuresystems

export PORTALNAME=hshioi # You need to modify your parameters
export PROJECTID=fg465b # Your project ID
export VMID=003b # this is arbitorary identifier for your VM

module load openstack
module load python\2.7

source .cloudmesh/clouds/india/juno/fg465
source ~/.cloudmesh/clouds/india/juno/openrc.sh

# Add security rule 
nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0
nova secgroup-add-rule default tcp 22 22 0.0.0.0/0
nova secgroup-add-rule default tcp 8888 8888 0.0.0.0/0
nova secgroup-add-rule default tcp 5000 5000 0.0.0.0/0
nova keypair-add --pub-key ~/.ssh/id_rsa.pub $USER-india-key
nova boot --flavor m1.small --image "futuresystems/ubuntu-14.04" 
--key_name $USER-india-key $USER-$VMID
nova floating-ip-create ext-net

export MYIP1=`nova floating-ip-list | grep "| -" | cut -d '|' -f3 | 
head -1`
nova add-floating-ip $USER-$VMID $MYIP1
nova show $USER-$VMID

echo '--- Connect VM ---'
echo 'Type: ssh -A -i ~/.ssh/id_rsa -l ubuntu $MYIP1'
