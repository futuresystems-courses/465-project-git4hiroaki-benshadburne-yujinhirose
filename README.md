# Open Source for Airline Delays with Hadoop

## 1 Goal & Project Overview
The goal of this project is to automate the task of creating virtual clusters on OpenStack and installing Apache Hadoop on the clusters. In addition we automize process importing airline data and utilize Python useful libraries to predict airline delays. 


1. Take raw data of page view statistics from airline database http://stat-computing.org/dataexpo/2009/the-data.html Dataset is related to airline statistics from 1987 to 2008 (i.e. date, Departure time, Tail Num, AirTime, Destination) 
2.	Create VM using OpenStack 
3.	Install OpenStack or Openstack client on VM
4.	Deploy 3-nodes Hadoop cluster with Python Libries
5.	Extract, transfer, and load datasets to Hadoop Distributed File System (HDFS)
6.	Transform raw data into reasonable feature using Pig - skip
7.	Execute python analysis code on a virtual cluster using Python libraries - skip
8.	Output on command line



## 2 Cloudmesh-plugin dataload instruction
Cloudmesh is installed

### 2-1 Pre-requisite


### 2-2 Installation instruction


### 2-1 Usage



## 3 Cloudmesh-plugin python_analze instruction


1. Make a copy of our project library from github. It can be found at
https://github.com/futuresystems/465-project-git4hiroaki-benshadburne-yujinhirose.git

Example command to copy library:
```
git clone https://github.com/futuresystems/465-project-git4hiroaki-benshadburne-yujinhirose.git
```
2. Change directories into our project folder.

```
cd github.com/futuresystems/465-project-git4hiroaki-benshadburne-yujinhirose.git
```


3. Run bash file for setup "start-clusters.sh" on your bash.
```
source start-cluster.sh
```


