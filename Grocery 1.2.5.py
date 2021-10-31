"""Made Minor changes from grocery 1.2 - grocery 1.2.5 
from now the program outputs file which stores the items entered with proper bill.... 
TL;DR Every time you use 'bill' option the program will save the items and rate in text file whose name is same of the present date and will be stored locally.... also the 'bill' function now will reset the items and rate after appending those information to the '.txt' file If u face any problems while using program do ping me... am on reddit u/anirudhp06 """


import sys
import datetime#Required For file generation
class grocery:
    today=datetime.date.today()#To fetch the date 
    file=open("{}.txt".format(today),"a+")#Will create a file with corresponding date
    file.write("{} Loggigng of expenditure started\n\n".format(datetime.datetime.now()))#First Line of the file
    a=[]#To store Name of Items
    b=[]#To store rate of corresponding Items
    bill=0
    serial=0
    choice=0#Use this in further Input
    def order(self):
        print("Name of Item:")
        nome = input()
        self.a.append(nome)#Append the item name to the list
        print("Rate of Item:")
        rate = int(input())
        self.b.append(rate)#Append the rate of the same item to list

    def display(self):
        series=0
        if self.a == []:
            print("Your Bucket List is empty! Insert Item")
        else:
            for i in range(0, len(self.a)):
                series+=1
                print("{}. {},{}/-".format(series,self.a[i], self.b[i]))

    def billl(self):
        self.bill= 0 # Again Re-Initializing bill to 0
        for i in self.b:
            self.bill += i #adding up all the rate from List b
        print("\t\tYour Bill is :", self.bill, "/-")
        self.file.write("List of items and its rate:\n")
        for i in range(len(self.a)):
            self.file.write("{},{}/-\n".format(self.a[i],self.b[i]))#Writes Items and its rate 
        self.file.write("Total Bill:{}".format(self.bill))#Writes total bill in '.txt' file
        self.file.write("\n\n")
        self.a.clear()#Clears out the items from list
        self.b.clear()#Clears out the rate of items from list
		

    def remove(self):
        if self.a == []:
            print("Your Bucket List is empty! Insert Item")
        else:
            self.serial = int(input("Enter Serial Number of Item to remove:"))
            if self.serial > len(self.a):
                print("Out of Range Try again")
            else:
                self.serial=self.serial-1
                self.a.remove(self.a[self.serial])
                self.b.remove(self.b[self.serial])
                print("List Updated")

    def edit(self):
        self.serial=int(input("Enter Serial Number of Item to edit:"))
        if self.serial>len(self.a):
            print("Out of Range Try again")
        else:
            self.serial=self.serial-1
            print("What do u want to change? \n1.Name\n2.Rate\n3.Both")
            bol=int(input())
            if bol==1:
                self.a.remove(self.a[self.serial])
                new_nome=input("Enter New name for it:")
                self.a.insert(self.serial,new_nome)
                print("List Updated")


            elif bol==2:
                self.b.remove(self.b[self.serial])
                new_rate = int(input("Enter New rate to it:"))
                self.b.insert(self.serial,new_rate)
                print("Rate Updated")

            elif bol==3:
                self.a.remove(self.a[self.serial])
                new_nome = input("Enter New name for it:")
                self.a.insert(self.serial, new_nome)
                print("Name Updated")
                self.b.remove(self.b[self.serial])
                new_rate=int(input("Enter New rate to it:"))
                self.b.insert(self.serial,new_rate)
                print("Rate Updated")


    def input(self):
        while self.choice!=6:
            print("\n\n1.Insert Grocery\n2.Display Bucket List\n3.Total Bill\n4.Remove item\n5.Edit Item\n6.Exit")
            self.choice=int(input("\nEnter Choice:"))
            if self.choice==1:
                self.order() #Calling all the functions

            elif self.choice==2:
                self.display()

            elif self.choice==3:
                self.billl()

            elif self.choice==4:
                self.remove()

            elif self.choice==5:
                self.edit()

            elif self.choice==6:
                print("Program Terminated")
				self.file.close()
                sys.exit()
            else:
                print("Try Again")

obj=grocery()
obj.input()