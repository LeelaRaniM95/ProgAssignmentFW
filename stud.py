import json
import time


print("welcoome!!!...opening the  INITIAL Key-value pair datastore\n\n")
with open('db2.json') as k:
    data = json.load(k)
    print(data)
temp=data
#for stud in data['studentdetails']:
    #print(stud['sname'],stud['branch'],  stud['sid']) 
print("\nwhat operations do you want to perform on key-value pair datastore..?")
print("select your choice.....!!!...")





def create():
    items={}
    with open("new.json", "r") as fr:
        d=json.load(fr)
    items["sname"]=input("enter student name")
    items["sid"]=int(input("enter student id"))
    items["percentage"] = int(input("enter student percentage"))
    items["branch"] =input("enter branch ")
    j=items['sid']
    for each in d:
        p=each['sid']
        if(j==p):
            print("ERROR:...Student ID already Existed....")
            break
        else:
            d.append(items)
            with open("new.json", "w") as fr:
                json.dump(d, fr, indent=5)
            print(d)
            break
      
            
    



def read(k):
    with open("new.json","r") as f:
        data=json.load(f)
    t={}
    t=data
    for each in t:
        if k not in each:
            print("Key is not found")
        else:
            b=each[k]
            print(b)
            break
            




def delete():
      display()
      new_data=[]
      with open("new.json", "r") as f:
          data=json.load(f)
          data_len=len(data)-1
      print("Which index number would you like to delete?")
      delind=input(f"select index number to delete 0-{data_len}")
      i=0
      for each in data:
          if i == int(delind):
              pass
              i=i+1
          else:
              new_data.append(each)
              i=i+1
      with open("new.json", "w") as f:
          json.dump(new_data, f, indent=4)
      print("Datastore after deleted key& its corresponding value")
      print(new_data)



def display():
    with open("new.json", "r") as f:
        data=json.load(f)
    i=0
    for each in data:
        #name=each['sname']
        ##branch=each['branch']
        #perc=each['percentage']
        print(f"The indexx numberis{i}")
        print(each)
        #print("sid :",id)
        ##print("perc :",perc)
        #print("\n\n")
        i=i+1



def update():
    with open("new.json", "r") as f:
        data=json.load(f)
    with open("db2.json", "r") as k:
        datab=json.load(k)
    datab+=data
    print(datab)

while True:
    c=int(input("1.CREATE" " ""  ""2.READ" "  " "3.DELETE"  "  " "4.EXIT" "  " "5.DISPLAY" "  " "6.UPDATED DATASTORE"))
    if c == 1:
        create()
    if c == 2:
        k=input("enter key")
        read(k)
    if c == 3:
        delete()
        print("key is deleted")
        print("\n\n")
    if c == 4:
        break
    if c == 5:
        display()
    if c == 6:
        print("...........The final keyvalue pair data store after all operations is........\n")
        update()


   
    





    