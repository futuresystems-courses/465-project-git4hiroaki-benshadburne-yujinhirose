echo '--- Set up VM from scratch --- Process (1)' 

if [ -z $VMID ]; then
    source config.sh
    echo "\$VMID is not provided: running config_v1.sh"
fi



nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0
nova secgroup-add-rule default tcp 22 22 0.0.0.0/0
nova secgroup-add-rule default tcp 8888 8888 0.0.0.0/0
nova secgroup-add-rule default tcp 5000 5000 0.0.0.0/0

nova keypair-add --pub-key ~/.ssh/id_rsa.pub $USER-india-key
nova boot --flavor m1.small --image "futuresystems/ubuntu-14.04" --key_name $USER-india-key $USER-$VMID
nova floating-ip-create ext-net

export MYIP=`nova floating-ip-list | grep "| -" | cut -d '|' -f3 | head -1`
# export MYIP=149.165.159.3
nova add-floating-ip $USER-$VMID $MYIP
nova show $USER-$VMID

echo '--- Connect VM ---'
echo 'Type: ssh -A -i ~/.ssh/id_rsa -l ubuntu $MYIP' 
ssh -A -i ~/.ssh/id_rsa -l ubuntu $MYIP

