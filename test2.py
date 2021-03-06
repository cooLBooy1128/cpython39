import os
import subprocess
import sys


def usage():
    print('At least 2 arguments (incl. cmd name).')
    print('usage: args.py arg1 arg2 [arg3... ]')
    sys.exit(1)


if __name__ == '__main__':
    # ret = os.system('ip')
    # print(f'{ret = }')
    argc = len(sys.argv)
    if argc < 3:
        usage()
    print("number of args entered:", argc)
    print("args (incl. cmd name) were:", sys.argv)
