import os
import sys

platformOS = sys.platform

if platformOS == 'linux':
    pat = '/home/drak/'
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

def find_pic(file_list):

    template = '.jpg'

for count in range(0, len(file_list)):
    if file_list[count].search(template, file_list[count]) > 0:
        print('pliki jpg'+file_list[count])

if __name__ == '__main__':
    try:
        what_is_what(pat)
    except:
        pass

find_pic(file_list)
print(dir_list)
print(file_list)
print(os.getcwd())