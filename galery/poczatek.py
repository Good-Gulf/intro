import os
import sys

platformOS = sys.platform

if platformOS == 'linux':
    pat = '/home/drak'
elif platformOS == 'win32':
    pat = 'c:/'

dir_list = []
file_list = []
pict_list = []
template = 'jpg'
pic = str


def what_is_what(pat):
    try:
        os.chdir(pat)
        ListOfAll = list(os.listdir())
        for count in range(0, len(ListOfAll)):
            if os.path.isfile(ListOfAll[count]):
                file_list.append(ListOfAll[count])
            else:
                dir_list.append(ListOfAll[count])
    except:
        print('ERROR - Brak Dostępu')


def change_path():

    tmpppath = pat
    newpath = pat
    try:
        os.chdir( pat + '/' + dir_list[count])
    except:
        print('Error - brak dostepu')


def find_pic(ext,files_list):

    count = 0

    print('testowanie')
    print(file_list)
    print(dir_list)
    for count in range(0,len(files_list)):
        if files_list[count].split('.')[-1] == ext:
            print('testowanie-loop')
            pict_list.append(os.getcwd()+'/'+files_list[count])
    return pict_list


if __name__ == '__main__':

    what_is_what(pat)
    find_pic(template,file_list)
print('test3')
print(file_list)
print(os.getcwd())
print(pict_list)
for count in range(0,len(pict_list)):
    print(pict_list[count])
