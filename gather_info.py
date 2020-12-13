#!/usr/bin/env python3
"""
module which will gather all needed data from an entity
"""
import os
import subprocess
import sp_utils as utils

class Server():
    """Store server information"""
    def __init__(self):
        pass

    def get_os_version(self):
    """Return OS version"""
        try:
            return subprocess.check_output("""sh -c '. /etc/os-release; echo "$VERSION"'""", shell=True, universal_newlines=True).strip()
        except subprocess.CalledProcessError as e:
            print('Cannot get OS version. Make sure /etc/os-release has VERSION="<INSTALLED_OS>" line')
        
    def get_platform(self):
    """Return server platform"""
        try:
            return subprocess.run()

myserver = Server()
print(myserver.get_os_version())
