"""
Library for the robot based system test tool of the OpenDaylight project.
Authors: Baohua Yang@IBM, Denghui Huang@IBM
Updated: 2013-11-14
"""
import collections

# Global variables
DEFAULT_CONTROLLER_IP = '127.0.0.1'
#DEFAULT_CONTROLLER_IP = '9.186.105.113' #just for temp test
DEFAULT_PORT = '8080'
DEFAULT_PREFIX = 'http://' + DEFAULT_CONTROLLER_IP + ':' + DEFAULT_PORT
DEFAULT_CONTAINER = 'default'
DEFAULT_USER = 'admin'
DEFAULT_PWD = 'admin'
MODULES_DIR = 'modules'
TIMEOUTS = 2

'''
Common constants and functions for the robot framework.
'''

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

def combine_strings(*strings):
    """
    Combines the given `strings` together and returns the result.
    The given strings are not altered by this keyword.
    """
    result = ''
    for s in strings:
        if isinstance(s,str) or isinstance(s,unicode):
            result += s
    if result == '':
        return None
    else:
        return result

if __name__ == '__main__':
    pass
