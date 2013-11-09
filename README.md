robot_tool
==========
*robot test tool for OpenDaylight Project.*

* Version: 0.1
* Authors: [Baohua Yang](mailto:yangbaohua@gmail.com), [Denghui Huang](mailto:huangdenghui@gmail.com)
* Homepage: <https://github.com/yeasy/robot_tool>

##Get Code

`git clone https://github.com/yeasy/robot_tool.git`

##Usage
###Prerequisites
* Python 2.6/2.7
* Python [Requests library](http://www.python-requests.org)

  ` pip install requests`

* [OpenDaylight Controller](https://wiki.opendaylight.org/view/GettingStarted:Developer_Main)
   * Download and build OpenDaylight Controller

   ```
   git clone https://git.opendaylight.org/gerrit/p/controller.git
   cd controller/opendaylight/distribution/opendaylight
   mvn clean install -DskipTests -Dmaven.compile.fork=true -U
   ```
* [Mininet](http://mininet.org/walkthrough/)
* [Robotframework](http://robotframework.org/)

###Run Test
* Start the [OpenDaylight Controller](https://wiki.opendaylight.org/view/GettingStarted:Developer_Main)

 ```
  cd controller/target/distribution.opendaylight-0.1.0-SNAPSHOT-osgipackage/opendaylight/
  ./run.sh
  ```
  
##Code Description

##Development Plan
* TODO

##About OpenDaylight
OpenDaylight is the first production-quality open-source SDN management platform sponsored by Linux Foundation. 
Lead SDN enterprises (Ericsson, IBM, Microsoft, Redhat, Cisco, Juniper, NEC, VMWare etc.) are involved to develop and support the project.
Please go to the official [homepage](http://www.opendaylight.org) page to find more information.
