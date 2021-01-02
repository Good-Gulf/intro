import os
import sys

platformOS = sys.platform

if platformOS == 'linux':
    pat = '/'
elif platformOS == 'win32':
    pat = 'c:'

dir_list = []
file_list = []


def what_is_what(pat):
    try:
        os.chdir(pat)
        ListOfAll = list(os.listdir())
    except:
        print('ERROR - Brak Dostępu')
    for count in range(0, len(ListOfAll)):
        if os.path.isfile(ListOfAll[count]):
            file_list.append(ListOfAll[count])
        else:
            dir_list.append(ListOfAll[count])


def change_path():

    tmpppath = pat
    newpath = temppath
    try:
        os.chdir( pat + '/' + dir_list[count])
    except:
        print('Error - brak dostepu')


if __name__ == '__main__':
    try:
        what_is_what(pat)
    except:
        pass

print(dir_list)
print(file_list)