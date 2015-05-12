# Load Modules
module load openstack
module load python\2.7

# Load your config (e.g., projectid, portalname) 
source .cloudmesh/clouds/india/juno/fg465
source ~/.cloudmesh/clouds/india/juno/openrc.sh

# VM setting
export VMID=team-byh-001b


echo "run setup_vm_v1.sh"
