#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import time

from beroot.run import check_all


if __name__ == '__main__':

    banner = '''
|====================================================================|
|                                                                    |
|                      Linux Privilege Escalation                    |
|                                                                    |
|                          ! BANG BANG !                             |
|                                                                    |
|====================================================================|
'''
    parser = argparse.ArgumentParser(description='%s\nFind a way to BeRoot' % banner, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--version', action='version', version='%(prog)s 1.1')
    parser.add_argument('--password', dest='password', help='if no NOPASSWD in sudoers, sudo -ll needs user password')

    arguments = parser.parse_args()
    start_time = time.time()

    print(banner)
    check_all(arguments.password)

    elapsed_time = time.time() - start_time
    print('Elapsed time = %s' % elapsed_time)
