
# This file contains all the utility methods that are
# used by 'airflow'.
# This file also contains global level constants.
#
# @author  Swayam Raina


NEWLINE = '\n'
FORWARD_SLASH = '/'
ANGULAR_START = '<'
ANGULAR_END = '>'
UTF8 = 'utf-8'
EQUALS = '='

def extract_branch_name(content, index):
    if content[-1] == NEWLINE:
        return content[index+1 : -1]
    return content[index+1 : ]

def extract_port(key_value_property):
    index = key_value_property.find( EQUALS )
    return key_value_property[ index+1 : ]