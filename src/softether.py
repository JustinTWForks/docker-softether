#!/usr/bin/env python3
import sys
import os
import subprocess as sp
import logging
import time
from pathlib import Path
from shutil import copyfile
import json
import random
import sys

sys.path.append('/opt/sylab/system')
from utils.install import setup_log_rotation, setup_systemd, init_log, remove_log_rotation, remove_systemd

def mk_service_dirs():
    sndir = str(Path(os.path.abspath(__file__)).parents[1])
    log_dir = sndir + '/log/softether'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    config_dir = sndir + '/configs/vpn_server'
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

def main(argv):
    time.sleep(99999)
    pass

if __name__ == "__main__":
    service_name = 'softether'
    for argv in sys.argv:
        if argv == '-i' or argv == 'install':
            setup_log_rotation(service_name)
            setup_systemd(service_name)
            mk_service_dirs()
            print('insstall success !!')
            exit()
        if argv == '-u' or argv == 'uninstall':
            remove_log_rotation(service_name)
            remove_systemd(service_name)
            print('remove success !!')
            exit()

    init_log(service_name)
    main(sys.argv)

