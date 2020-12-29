import os
import sys

platformOS = sys.platform

if platformOS == 'linux':
    pat = '/'
elif platformOS == 'win32':
    pat = 'c:'

def dirlist(pat):
    os.chdir(pat)
    l = list(os.listdir())
    hisPat = []
    print(l)
    count = 0
    for count in range(0, len(l)):
        newpat = pat+'/'+l[count]
        hisPat.append(newpat)
        try:
            os.chdir(newpat)
        except:
            print('error 13 - Permission denied')
            pat=hisPat[count-1]
        count = count+1
        pat = l[count - 1]
        print(newpat)
        print(l)
        print(count)
        print(hisPat)

def dirtree():
    for (root,dirs,files) in os.walk('Test', topdown=True):
        print (root)
        print (dirs)
        print (files)
        print ('--------------------------------')

if __name__ == '__main__':
    dirlist(pat)
    # dirtree()

    # for root, dirs, files in os.walk(".", topdown=False):
    #     for name in files:
    #         print(os.path.join(root, name))
    #     for name in dirs:
    #         print(os.path.join(root, name))