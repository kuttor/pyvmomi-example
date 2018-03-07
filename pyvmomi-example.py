#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" pyvmomi_examples.py

Usage:
    pyvmomi_example <sub-command>

Options:
  -h --help     Show this screen
  --version     Show version

"""

__author__ = "Andrew Kuttor"
__credits__ = "Andrew Kuttor"
__email__ = "andrew.kuttor@dimensiondata.com"
__status__ = "Prototype"
__version__ = "0.0.1"
__maintainer__ = "Andrew Kuttor"

from pyVim.connect import SmartConnect as connect
from pyVim.connect import Disconnect as kill


def list_vms():
    datacenter = c.content.rootFolder.childEntity[0]
    vms = datacenter.vmFolder.childEntity

    for vm in vms:
        print(vm.name)


def main(host, user, pwd):
    creds = {host, user, pwd}

    connect(**creds)
    list_vms()
    kill(connect(**args))


if __name__ == '__main__':
    main()
