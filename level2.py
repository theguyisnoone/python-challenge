import re

def wash(fname,wname):
    f=open(fname)
    a=""
    ##soluation1:
    for line in f:
        pa=re.compile(r'[a-zA-Z]')
        ma=pa.findall(line)
        for c in ma:
            a+=c

    ##soluation2
    x=f.read()
    for i in x:
        res=i.isalpha()
        if res == True:
            a += i
    print(a)

    #all 
    w=open(wname,'w')
    w.write(a)
    w.close()
    f.close()

wash("messup.txt","limpia.txt")
