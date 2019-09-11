#!/usr/bin/env python3

import sys

def copy_file(scr, dst):
    with open(scr, 'r') as scr_file:
        with open(dst, 'w') as dst_file:
            dst_file.write(scr_file.reaadlines())


if __name__ == '__main__':
    if len(sys.argv) == 3:
        copy_file(sys.argv[1],sys.argv[2])

    else:
        print('Parameter Error')
        print(sys.argv[0], 'srcfile detfile')
        sys.exit(-1)
    sys.exit(0)

