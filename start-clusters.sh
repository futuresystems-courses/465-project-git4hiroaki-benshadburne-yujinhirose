source config.sh

echo Creating Stack for $HEATUSERNAME

# As "KeyName", you need to check what name your public key is registered in India
# Please make sure to match the belwo finger prints
# 1. ssh-keygen -lf ~/.ssh/id_rsa.pub
# 2. nova keypair-list
heat stack-create --template-file hadoop-cluster-airline-del-pred.yaml -P "KeyName=`cat $KeyName`;PublicKeyString='cat $HEATPUBKLOC';PrivateKeyString='cat $HEATPVTKLOC';Hadoop1Name="Hadoop1-$HEATUSERNAME";Hadoop2Name="Hadoop2-$HEATUSERNAME";Hadoop3Name="Hadoop3-$HEATUSERNAME"" analysis-hadoops-$HEATUSERNAME



