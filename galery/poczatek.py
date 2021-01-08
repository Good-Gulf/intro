import os
import sys

platformOS = sys.platform

if platformOS == 'linux':
    pat = '/home/drak'
elif platformOS == 'win32':
    pat = 'c:'

dir_list = []
file_list = []
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
    # picture = str
    # fl = files_list

    print('testowanie')
    print(file_list)
    print(dir_list)
    for count in range(0,len(files_list)):
        if files_list[count].split('.')[-1] == ext:
            print('testowanie-loop')
            print(files_list[count])
        # print(fl[count])

    # for count in range(0,len(file_list)):
    #     found = re.search(template, file_list[count])
    #     if found:
    #         picture = found.group()
    #     print('plik '+file_list[count])
    #     print(picture)


if __name__ == '__main__':
    # try:
    #     # what_is_what(pat)
    #     find_pic(file_list,template)
    # except:
    #     find_pic(file_list,template)
    #     pass

    what_is_what(pat)
    find_pic(template,file_list)
print('test3')
print(file_list)
print(os.getcwd())