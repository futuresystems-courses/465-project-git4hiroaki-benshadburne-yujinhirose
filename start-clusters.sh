source config.sh

echo Creating Stack for $HEATUSERNAME

heat stack-create --template-file hadoop-cluster-airline-del-pred.yaml -P "KeyName=id_rsa;PublicKeyString='cat $HEATPUBKLOC';PrivateKeyString='cat $HEATPVTKLOC';Hadoop1Name="Hadoop1-$HEATUSERNAME";Hadoop2Name="Hadoop2-$HEATUSERNAME";Hadoop3Name="Hadoop3-$HEATUSERNAME"" flight-analysis-hadoop-cluster-$HEATUSERNAME



