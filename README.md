# Open Source for Airline Delays with Hadoop

## 1 Goal & Project Overview
The goal of this project is to automate the task of creating virtual clusters on OpenStack and installing Apache Hadoop on the clusters. In addition we automize process importing airline data and utilize Python useful libraries to predict airline delays. 


1.      Take raw data of page view statistics from airline database http://stat-computing.org/dataexpo/2009/the-data.html Dataset is related to airline statistics from 1987 to 2008 (i.e. date, Departure time, Tail Num, AirTime, Destination) 
2.	Create VM using OpenStack 
3.	Install OpenStack Heat client on your VM
4.	Deploy 3-nodes Hadoop cluster with Python libraries
5.	Extract, transfer, and load datasets to Hadoop Distributed File System (HDFS)
6.	Transform raw data into reasonable feature using Pig - skip
7.	Execute python analysis code on a virtual cluster using Python libraries - skip
8.	Output on command line



## 2 Cloudmesh-plugin dataload instruction



### 2-1 Pre-requisite    

* Cloudmesh is installed
* CMD3 is installed ([reference](http://cloudmesh.github.io/cmd3/manual.html#generating-independent-packages))

### 2-2 Step-by-step installation manual

Clone repository to your local directory and move on `cloudmesh_dataload` directory, and move on that directory. Then install the cloudmesh_dataload plugin. You can check the installation by `cm help` command. 

1. `git clone https://github.com/futuresystems/465-project-git4hiroaki-benshadburne-yujinhirose.git`
2. `cd 465-project-git4hiroaki-benshadburne-yujinhirose/cloudmesh_dataload`
3. Add `    - cloudmesh_deploy.plugins` as the last sentence in in `~/.cloudmesh/cmd3.yaml` 
4. `python setup.py install`
5. `cm plugins add cloudmesh_dataload`

### 2-3 Usage

This dataload plugin has simplest  functionality: download the data from a specified URL and delete data source. It is good for you to understand how cloudmesh plugins work.

- `cm dataload start [-url=U]`

This cm dataload command will start to download the data source by using `wget`. Default URL is set http://stat-computing.org/dataexpo/2009/2007.csv.bz2 but you can specify a URL of data source by using `-url=U` option.

- `cm dataload delete NAME`

This cm dataload command will delete your data source specified by `NAME`.


## 3 Automatic deployment for analysis environment with Pydoop

This section describes how to automatically deploy your analysis environment where Hadoop, Pig and other python libraries such as Pandas, Scikit-learn, Numpy, Matplotlib, Pydoop using OpenStack Heat. 

### 3-1 Pre-requisite    

* Cloudmesh installed on your virtual machine
* OpenStack accounts  

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

In India, 
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



1) Make a copy of our project repository and move on it. It can be found at
https://github.com/futuresystems/465-project-git4hiroaki-benshadburne-yujinhirose.git

```
git clone https://github.com/futuresystems/465-project-git4hiroaki-benshadburne-yujinhirose.git
cd 465-project-git4hiroaki-benshadburne-yujinhirose
```

2) Edit "config.sh" to specify the location of public and private key if necessary.

As for "KeyName" you can check the key name registered in India with commands `nova keypair-list`

```
nano config.sh
```

3) Run bash file for setup "start-clusters.sh" on your bash.

```
source start-cluster.sh
```

If you succeed to run this command appropriately, you can find your stack, named "flight-analysis-hadoop-[your name]" by `heat stack-list`



## Data source
The data is Airline on-time performance data since our focus is to automate construction process for predicting airline delays. You can choose data source from 1987 to 2008 ([data source link]( http://stat-computing.org/dataexpo/2009/the-data.html)) Each of the data field is described as well.

#### Sample of data
| Year | Month | DayofMonth | DayOfWeek | DepTime | CRSDepTime | ArrTime | CRSArrTime | UniqueCarrier | FlightNum | TailNum | ActualElapsedTime | CRSElapsedTime | AirTime | ArrDelay | DepDelay | Origin | Dest | Distance | TaxiIn | TaxiOut | Cancelled | CancellationCode | Diverted | CarrierDelay | WeatherDelay | NASDelay | SecurityDelay | LateAircraftDelay |
|------|-------|------------|-----------|---------|------------|---------|------------|---------------|-----------|---------|-------------------|----------------|---------|----------|----------|--------|------|----------|--------|---------|-----------|------------------|----------|--------------|--------------|----------|---------------|-------------------|
| 2008 | 1     | 3          | 4         | 2003    | 1955       | 2211    | 2225       | WN            | 335       | N712SW  | 128               | 150            | 116     | -14      | 8        | IAD    | TPA  | 810      | 4      | 8       | 0         |                  | 0        | NA           | NA           | NA       | NA            | NA                |
| 2008 | 1     | 3          | 4         | 754     | 735        | 1002    | 1000       | WN            | 3231      | N772SW  | 128               | 145            | 113     | 2        | 19       | IAD    | TPA  | 810      | 5      | 10      | 0         |                  | 0        | NA           | NA           | NA       | NA            | NA                |
| 2008 | 1     | 3          | 4         | 628     | 620        | 804     | 750        | WN            | 448       | N428WN  | 96                | 90             | 76      | 14       | 8        | IND    | BWI  | 515      | 3      | 17      | 0         |                  | 0        | NA           | NA           | NA       | NA            | NA                |

## Technologies

* OpenStack 
* OpenStack Heat client
* Cloudmesh
* Hadoop & HDFS
* Pig
* Python with libraries (e.g., Pandas, Scikit-learn, Numpy, Matplotlib. Pydoop)



## Reference


- Project reference "Predicting Airline Delays with Hadoop": http://cloudmesh.github.io/introduction_to_cloud_computing/projects/sample_project_airline_delays.html

- Heat template deploying hadoop clusters:  https://github.com/cloudmesh/cloudmesh/blob/master/heat-templates/ubuntu-14.04/hadoop-cluster/hadoop-cluster.yaml 

- OpenStack clients: https://github.com/openstack/python-heatclient

- Pig: http://pig.apache.org/docs/r0.7.0/setup.html

- Hadoop: http://hadoop.apache.org/

- Pydoop: http://crs4.github.io/pydoop/installation.html
