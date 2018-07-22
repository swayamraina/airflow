
# This file contains all the handler functions for 'airflow'. 
# All the requested commands are redirected to their corresponding
# handler methods for execution.
#
# @author  Swayam Raina


import argparse

from os_utils import (
    get_instance_dir,
    get_git_branch_name,
    get_git_branch_owner,
    get_instance_port,
    get_pid_from_port,
    stop_server
)

from os_commands import (
    GIT_BRANCH_FILE_PATH,
    GIT_LOG_FILE_PATH
)

from config import (
    SERVER_PORT_FILEPATH
)

from utils import (
    FORWARD_SLASH
)

def heartbeat_handler(args: argparse.Namespace):
    pass

def start_handler(args: argparse.Namespace):
    pass

'''
    This method is responsible for shutting down a 
    specific server. 
'''
def stop_handler(args: argparse.Namespace):
    server_name = getattr(args, 'server_name')
    instance_dir = get_instance_dir(server_name)
    application_properties_path = instance_dir +  FORWARD_SLASH + SERVER_PORT_FILEPATH
    instance_port = get_instance_port(application_properties_path)
    pid = get_pid_from_port(instance_port)
    status = stop_server(pid)
    print(status)

def restart_handler(args: argparse.Namespace):
    pass


'''
    This particular method is responsible for displaying 
    the branch deployed on the instance and the owner of
    the branch.
'''
def git_handler(args: argparse.Namespace):
    server_name = getattr(args, 'server_name')
    instance_dir = get_instance_dir(server_name)
    branch_name_path = instance_dir +  FORWARD_SLASH + GIT_BRANCH_FILE_PATH
    owner_name_path = instance_dir + FORWARD_SLASH + GIT_LOG_FILE_PATH
    print('Current deployed branch : ' + get_git_branch_name(branch_name_path))
    print('Owner of the branch : ' + get_git_branch_owner(owner_name_path))


def logs_handler(args: argparse.Namespace):
    pass


def deploy_handler(args: argparse.Namespace):
    pass


if __name__ == '__main__':
    pass