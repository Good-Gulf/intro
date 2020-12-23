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
    print(l)
    count = 0
    for count in range(0, len(l)):
        pat = pat+'/'+l[count]
        count = 0
        os.chdir(pat)
        l = list(os.listdir())
        print(pat)
        print(l)

def dirtree():
    for (root,dirs,files) in os.walk('Test', topdown=True):
        print (root)
        print (dirs)
        print (files)
        print ('--------------------------------')

if __name__ == '__main__':
    # dirlist(pat)
    # dirtree()

    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))