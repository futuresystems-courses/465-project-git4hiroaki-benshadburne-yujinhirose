# Open Source for Airline Delays with Hadoop

## 1 Goal & Project Overview
The goal of this project is to automate the task of creating virtual clusters on OpenStack and installing Apache Hadoop on the clusters. In addition we automize process importing airline data and utilize Python useful libraries to predict airline delays. 


1.      Take raw data of page view statistics from airline database http://stat-computing.org/dataexpo/2009/the-data.html Dataset is related to airline statistics from 1987 to 2008 (i.e. date, Departure time, Tail Num, AirTime, Destination) 
2.	Create VM using OpenStack 
3.	Install OpenStack or OpenStack client on VM
4.	Deploy 3-nodes Hadoop cluster with Python libraries
5.	Extract, transfer, and load datasets to Hadoop Distributed File System (HDFS)
6.	Transform raw data into reasonable feature using Pig - skip
7.	Execute python analysis code on a virtual cluster using Python libraries - skip
8.	Output on command line



## 2 Cloudmesh-plugin dataload instruction (Yujin)

Cloudmesh is installed

### 2-1 Pre-requisite    


### 2-2 Step-by-step installation manual


### 2-3 Usage



## 3 Cloudmesh-plugin python_analze instruction (Yujin )

### 3-1 Pre-requisite    


### 3-2 Setup OpenStack Heat client

1. Install OpenStack Heat Client using pip

```
vm$ sudo pip install python-heatclient
```

2. Read environment variables from openrc.sh

When you install cloudmesh, 'cm-iu user fetch', 'cm-iu user create' are supposed to copy your "openrc.sh" file from india to your virtual machine. 

```
vm$ source  ~/.cloudmesh/clouds/india/openrc.sh  
```
3. Set "OS_CACERT" variable

We need to copy certification information from india, which is specified by "OS_CACERT" in "openrc.sh".

In Idia, 
```
india$ echo $OS_CACERT
```

In your vm, paste the content of cacert.pem to ~/.cloudmesh/clouds/india/juno/cacert.pem

```
vm$ mkdir ~/.cloudmesh/clouds/india/juno # create juno directory
vm$ nano ~/.cloudmesh/clouds/india/juno/cacert.pem # Paste "cacert.pem" from india
```

4. Test heat commands in your vm

```
vm$ heat stack-list
```

* reference: http://docs.rackspace.com/orchestration/api/v1/orchestration-getting-started/content/Install_Heat_Client.html

### 3-3 Usage



1) Make a copy of our project library from github. It can be found at
https://github.com/futuresystems/465-project-git4hiroaki-benshadburne-yujinhirose.git

Example command to copy library:
```
git clone https://github.com/futuresystems/465-project-git4hiroaki-benshadburne-yujinhirose.git
```

2) Change directories into our project folder.

```
cd 465-project-git4hiroaki-benshadburne-yujinhirose
```

3) Edit "config.sh" to specify the location of public and private key if necessary.

As for "KeyName" you can check the key name registered in India with commands "nova keypair-list"

```
nano config.sh
```

4) Run bash file for setup "start-clusters.sh" on your bash.

```
source start-cluster.sh
```

## 4 Heat-temlate


1.	Create VM using OpenStack 

2.	Install OpenStack or Openstack client on VM

3.	Deploy 3-nodes Hadoop cluster with Python Libries

4.	Extract, transfer, and load datasets to Hadoop Distributed File System (HDFS)


## 5 Reference


- Project reference "Predicting Airline Delays with Hadoop": http://cloudmesh.github.io/introduction_to_cloud_computing/projects/sample_project_airline_delays.html

- Heat template deploying hadoop clusters:  https://github.com/cloudmesh/cloudmesh/blob/master/heat-templates/ubuntu-14.04/hadoop-cluster/hadoop-cluster.yaml 

- OpenStack clients: https://github.com/openstack/python-heatclient

- Pig: http://pig.apache.org/docs/r0.7.0/setup.html

- Hadoop: http://hadoop.apache.org/

- Pydoop: http://crs4.github.io/pydoop/installation.html
