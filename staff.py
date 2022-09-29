'''consider the following definition of dictionary staff and write the method in python
1. To search and display the content in a pickled file 'staff.dat'
where staffcode key of the dictionary is matching with 'S0105'
structure:  staff={'staffcode': ...,'Name': ...}
'''
import pickle as p
def f1():
     x=open("staff.dat","ab")
     d={}
     c=input("Enter staffcode: ")
     n=input("Enter name: ")
     d['staffcode']=c
     d['name']=n
     p.dump(d,x)
     x.close()

def f2():
     r=open("staff.dat","rb")
     try:
          while True:
               d=p.load(r)
               print(d)
     except:
          r.close()
def f3():
     x=open("staff.dat","rb")
     f=0
     try:
          while True:
               d=p.load(x)
               if d['staffcode']=='S0105':
                    print(d)
                    f=1
     except:
          x.close()
     if f==0:
          print('No matching record found')

def f4():
     s=input("Record to be modified: ")
     r=[]
     si=open("staff.dat","rb")
     f=0
     try:
          while True:
               d=p.load(si)
               if d['staffcode']==s:
                    print(d)
                    n=input("Enter new name: ")
                    d['name']=n
                    f=1
               r.append(d)
     except:
          si.close()
     if f==0:
          print('No matching record found: ')
     si=open("staff.dat","wb")
     for a in r:
          p.dump(a,si)


def  delete():
     s=input("Record to be deleted: ")
     r=[]
     si=open("staff.dat","rb")
     try:
          while True:
               d=p.load(si)
               if d['staffcode']==s:
                    continue
               else:
                    r.append(d)
     except:
          si.close()
          wi=open("staff.dat","wb")
          for i in r:
                p.dump(r,wi)
          wi.close()
          

     

               
