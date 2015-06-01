
read -p "What is your Username?: " Heat_Username
Hadoop1Name="Hadoop1-$Heat_Username"
Hadoop2Name="Hadoop2-$Heat_Username"
Hadoop3Name="Hadoop3-$Heat_Username"

read -p "Type Path to your PublicKey. (i.e. ~/.ssh/publickey): " Heat_PublicKey
Heat_PublicKey='cat $Heat_PublicKey'
read -p "Type Path to your PrivateKey. (i.e. ~/.ssh/privatekey): " Heat_PrivateKey
Heat_PrivateKey='cat $Heat_PrivateKey'

echo Creating Heat Stack for $Heat_Username

heat stack-create --template-file sample.yaml -P "KeyName=id_rsa;PublicKeyString=$Heat_PublicKey;PrivateKeyString=$Heat_PrivateKey;Hadoop1Name=$Hadoop1Name;Hadoop2Name=$Hadoop2Name;Hadoop3Name=$Hadoop3Name" flight-analysis-hadoop-cluster-$Heat_Username


