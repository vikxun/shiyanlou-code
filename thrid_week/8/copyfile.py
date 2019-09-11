#!/usr/bin/env python3

import sys


def copy_file(rst, wst):
    with open(rst, 'r') as rst_file:
        with open(wst, 'w') as wst_file:
            for a,b in enumerate(rst_file.readlines()):
                wst_file.write('{} {}'.format(a+1, b))

    
#            print(wst_file.readlines())

if __name__ == '__main__' :

    if len(sys.argv) == 3:
        copy_file(sys.argv[1], sys.argv[2])
        
    
        
    else:
        print('Parameter Error')
        sys.exit(-1)

    sys.exit(0)
"""    with open(sys.argv[2], 'r') as file1:
  #      print(file1.read())

        for a,b in enumerate(file1.readlines()):
            print('{} {}'.format(a+1, b), end = '')
"""

 

