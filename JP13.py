def write():
    f=open("JP13.txt","w")
    while True:
        n=input("Enter line=")
        f.write(n+"\n")
        o=""
        p=input("press enter to add more lines and anything else to escape")
        if p==o:
            continue
        else:
             break
def separate():
    f=open("JP13.txt","r")
    k=" "
    g="#"
    data=f.readlines()
    for i in data:
              p=i.replace(k,g)
              print(p,end="")


    

     

 
