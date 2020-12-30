import os
import sys

platformOS = sys.platform

if platformOS == 'linux':
    pat = '/'
elif platformOS == 'win32':
    pat = 'c:'

dir_list = []
file_list = []

def WhatIsWhhat(pat):
    os.chdir(pat)
    ListOfAll = list(os.listdir())
    for count in range(0, len(ListOfAll)):
        if os.path.isfile(ListOfAll[count]):
            file_list.append(ListOfAll[count])
        else:
            dir_list.append(ListOfAll[count])


if __name__ == '__main__':
    WhatIsWhhat("/home/drak")
    print(dir_list)
    print(file_list)