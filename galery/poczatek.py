import os

pat = '/home'
os.chdir(pat)
scierzka = os.getcwd()
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

if __name__ == '__main__':
    print(scierzka)
    # print (len(l))
    # print(l)