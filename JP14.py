"""To make a function that reads line from the user and
writes it into a binary file "JP14.dat" , after every
line ask user if he wish to continue in case of yes input line again and write it into the file if no
then print all the contents of the file"""
import pickle as p
def write():
     x=open("JP14.dat","ab")
     while True:
          d={}
          c=input("Enter line")
          p.dump(c,x)
          g=input("do u want to add more records  enter yes to add more no to exit")
          if g in "YESyes":
               continue
          else:
               x.close()
               f=open("JP14.dat","rb")
               try:
                    while True:
                         z=p.load(f)
                         print(z)
               except:
                         f.close()
                         break
               
     
     
          
          
