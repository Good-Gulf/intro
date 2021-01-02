import os
import sys

platformOS = sys.platform

if platformOS == 'linux':
    pat = '/'
elif platformOS == 'win32':
    pat = 'c:'

def dirlist(pat):
    os.chdir(pat) # os.chdir - Zmiana ścieżki dostępu na podana w parametrze jako str
    l = list(os.listdir())# przypisanie listy plików i katalogów z aktualnej lokalizacji do zmiennaj l
    hisPat = []
    print(l)
    count = 0
    for count in range(0, len(l)):
        newpat = pat+'/'+l[count]
        hisPat.append(newpat)
        # print('sciezka'+hisPat)
        try:
            os.chdir(newpat)
        except:
            print('error 13 - brak dostępu')
            pat=hisPat[count-1]
        count = count+1
        pat = l[count - 1]
        print(newpat)
        # print(l)
        # print(count)
        # print('sciezka'+hisPat)


if __name__ == '__main__':
    dirlist(pat)