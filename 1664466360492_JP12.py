'''JP 12-25.7.22
1.Make a function to read data and write in file jp12.txt.
2.Make a function to find a word used minimum no.of times in the given file.
'''
def f1():
    w=open("jp12.txt","a+")
    n=int(input("Enter no. of lines to input:"))
    for a in range(n):
        m=input("Enter the line:")
        w.write(m+'\n')
    w.close()
def f2():
    w=open("jp12.txt","r")
    a=w.read()
    print(a)
    a=a.split()
    w=[]
    minn=a.count(a[0])
    for i in a:
        if a.count(i)<minn:
            minn=a.count(i)
    for j in a:
        if a.count(j)==minn:
            w.append(j)
    print(w,minn)
            
    
