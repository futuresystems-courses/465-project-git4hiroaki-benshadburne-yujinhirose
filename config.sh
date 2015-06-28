#read -p "Please input your KeyName: " KeyName
KeyName=hshioi-ubuntu-vm-key
HEATUSERNAME=$OS_USERNAME
ssh-kegen -f temp.rsa -t -N ''
HEATPUBKLOC=./temp.rsa.pub
HEATPVTKLOC=./temp.rsa

