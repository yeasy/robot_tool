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
* Python [Roboframework-requests library](https://github.com/bulkan/robotframework-requests/)
 
  pip install -U robotframework-requests

* [OpenDaylight Controller](https://wiki.opendaylight.org/view/GettingStarted:Developer_Main)
   ```
   # Download and build OpenDaylight Controller
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
* Start mininet, and make sure mininet has all switches connected to the controller, for example, 
      `sudo mn --controller=remote,ip=your_controller_ip --topo tree,2`
*  Go to the suites directory, executing the suite such as `pybot --variable topo_tree_level:2 base` which will run all tests in the base edition or `pybot --variable topo_tree_level:2 switch_manager.txt` to test the switch manager module.
  
##Code Structure

    robot_tool
    \---------suites       # all robot test suites
    |         \-----base                # all test suites for the base edition
    |         |
    |         \-----service_provider    # all test suites for the service provider edition
    |         |
    |         \-----virtualization      # all test suites for the service provider edition
    |
    \---------libraries    # all keywords
    |
    \---------resources    # resources related files
    |
    \---------variables    # all variables

##Hack Code
###Create and import Library
The robotframework supports both Python and Java based library. Here we take the Python code for example.

The library can be either a normal module or a class (Commonly a *.py file). You can add the `Library    your_library_file` command into the `*** Settings ***` part to import a library. Notice the elements (variable, keyword, etc) separator in robot script is tab, instead of space. Space is only used inside the name of the same element. 

###Add Keyword
In case of a module, a keyword will be created for each top-level function in the module. In case of a class, a keyword will be created for each public method of the class.

Keyword name will be mapped to the function name (case insensitively and underscores removed), and the keywords will have same arguments as the functions. For example, if you define a function in the library as
```
def print_hello_world(param1,param2):
    """
    Just print out the first hello to the world.
    """
    print "Hello world",param1,param2
```
Then after import the library, you can use the keyword in the robot framework as
```
$param1    Hi
$param2    Again
Print Hello World     ${param1}    ${param2}
```

###Example Case
Some useful basic functions are defined in `libraries/Common.py` library.
You can see the code to find a `collection_should_contain` function (check if a collection should contain every given member) like
```
import collections
def collection_should_contain(collection, *members):
    """
    Fail if not every members is in the collection.
    """
    if not isinstance(collection, collections.Iterable):
        return False
    for m in members:
        if m not in collection:
            return False
    else:
        return True
```
Then we can use the keyword `Collection Should Contain` after importing the library as
`Library           ../../libraries/Common.py`.
For example, in the switch_manager.txt robot script.
```
Collection Should Contain    ${nodes}    ${topo_nodes}
```


###Learning More
Would like to suggest to read the [Python Tutorial for robotframework] (http://code.google.com/p/robotframework/wiki/PythonTutorial) and the [Robot Framework User Guide](http://code.google.com/p/robotframework/wiki/UserGuide).

##Development Plan
* Finish test suites for the base edition.

##About OpenDaylight
OpenDaylight is the first production-quality open-source SDN management platform sponsored by Linux Foundation. 
Lead SDN enterprises (Ericsson, IBM, Microsoft, Redhat, Cisco, Juniper, NEC, VMWare etc.) are involved to develop and support the project.
Please go to the official [homepage](http://www.opendaylight.org) page to find more information.


##Robot framework user guide.
   http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.8.1

##Testlibraries references.
   3.1 A list of available test libraries for Robot Framework 
   http://code.google.com/p/robotframework/wiki/TestLibraries
