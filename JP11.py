
"""
make a program with following functions
1.func1() to read lines from the user and write them into a file JP11.txt
2.func2() to copy those words to copy which begin with a vowel in copyjp11.txt
"""
def write():
    f=open("JP11.txt","w")
    while True:
        n=input("Enter line=")
        f.write(n+"\n")
        o=""
        p=input("press enter to add more lines and anything else to escape")
        if p==o:
            continue
        else:
            break
def copycat():
    f=open("copyjp11.txt","w+")
    p=open("JP11.txt","r")
    data=p.read().split()
    
    for i in data:
        if i[0] in "AEIOUaeiou":
            f.write(i+"\n")
    f.seek(0)
    print(f.read())
    
            

    
