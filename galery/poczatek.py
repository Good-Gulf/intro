import os

os.chdir('/home')
scierzka = os.getcwd()
l = list(os.listdir())
if __name__ == '__main__':
    print(scierzka)
    print(l)