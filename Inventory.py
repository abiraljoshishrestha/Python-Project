#Importing various modules
import Write
import Test
import Main

#Importing inbuilt functions
import random
import datetime

#Creating lists
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]


file=open("Inventory.txt","r") #opening file for reading data
for line in file:
    x=line.split("\n")
    a=x[0]
    list1.append(a)
file.close()

list2.append(list1[0])
list3.append(list1[1])
list4.append(list1[2])


for i in list2: #appending various data to different lists
    x=i.split(",")
    a=x[0]
    b=x[1]
    c=x[2]
    list5.append(a)
    list5.append(int(b))
    list5.append(int(c))

for i in list3: #appending various data to different lists
    x=i.split(",")
    a=x[0]
    b=x[1]
    c=x[2]
    list6.append(a)
    list6.append(int(b))
    list6.append(int(c))

for i in list4: #appending various data to different lists
    x=i.split(",")
    a=x[0]
    b=x[1]
    c=x[2]
    list7.append(a)
    list7.append(int(b))
    list7.append(int(c))


def menu(): #Creating a function to show menu
    print("Press 1 to purchase a product")
    print("Press 2 to see available stock")
    print("Press 3 to exit")
    return input("Enter your choice=")


def file(): #Creating a function to write a file
    a=("customer"+str(random.randint(1,100)))
    d=str(datetime.datetime.now())
    Write.file(a,name,choice,d,finalprice,discount,quantity)
        
   
#Using while in order to keep the programing running until users decides to quit
print(Main.inventory(list5,list6,list7))
while True:
    run=menu()
    if run=="1" or run=="one":
        choice1=input("Enter product you want to purchase=")
        choice=choice1.upper() #Calling a module to convert lowercase string to uppercase string
        if choice=="TV":
            if list5[1]>0:
                #Using exception handling to take correct input from the user
                success=False
                while success==False:
                    try:
                        quantity=int(input("Enter quantity="))
                        if quantity<=list5[1] and quantity>0:
                            success=True
                        else:
                            print("---------------------------------------------------------------")
                            print("Enter quantity is greater than or less than the available stock")
                            print("---------------------------------------------------------------")
                    except:
                        print("--------------------------------")
                        print("Please enter quantity in numbers")
                        print("--------------------------------")
                        
                print("Price=",list5[2])
                product=list5[1]
                q=product-quantity #Calling a module to manage quantity
                print("Quantity=",quantity)
                a=list5[2]
                s1=False
                while s1==False:
                    dis1=input("Has discount been given(yes/no)?")
                    dis=dis1.upper()       
                    if dis=="YES":
                        #Using exception handling to take correct input from the user
                        success=False
                        while success==False:
                            try:
                                discount=int(input("Enter discount amount="))
                                if discount<=list5[2] and discount>0:
                                    success=True
                                else:
                                    print("-----------------------------------------------------------------------")
                                    print("Discount amount cannot be greater than or less than the mentioned price")
                                    print("-----------------------------------------------------------------------")
                            except:
                                print("---------------------------------------")
                                print("Please enter discount amount in numbers")
                                print("---------------------------------------")
                        s1=True
                        
                    elif dis=="NO":
                        discount=0
                        s1=True

                    else:
                        print("error")
                        s1=False
                  
                price=a*quantity #Calling a module to find price by multiplying price with no of quantity
                finalprice=price-discount #Calling a module to find toatl price with discount
                print("Discount amount=",discount)
                print("Total Price=",finalprice)
                name1=input("Enter your name=")
                name=name1.upper() #Calling a module to convert lowercase string to uppercase string

                #Using exception handling to take correct input from the user
                s2=False
                while s2==False:
                    try:
                        final=input("Do you really want to purchase this product(yes/no)=")
                        final_choice=final.upper()
                        if final_choice=="YES":
                            list5[1]=q
                            file()
                            print("Thank you for your purchase")
                            s2=True
                        elif final_choice=="NO":
                            print(menus.stock(list5,list6,list7))
                            s2=True
                    except:
                        print("Error")
            else:
                print("----------------------")
                print("Currently not in stock")
                print("----------------------")
                
        elif choice=="LCD":
            if list6[1]>0:
                #Using exception handling to take correct input from the user
                success=False
                while success==False:
                    try:
                        quantity=int(input("Enter quantity="))
                        if quantity<=list6[1] and quantity>0:
                            success=True
                        else:
                            print("---------------------------------------------------------------")
                            print("Enter quantity is greater than or less than the available stock")
                            print("---------------------------------------------------------------")
                    except:
                        print("--------------------------------")
                        print("Please enter quantity in numbers")
                        print("--------------------------------")

                print("Price=",list6[2])
                product=list6[1]
                q=product-quantity#Calling a module to manage quantity
                print("Quantity=",quantity)
                a=list5[2]
                
                #Using exception handling to take correct input from the user
                s1=False
                while s1==False:
                    dis1=input("Has discount been given(yes/no)?")
                    dis=dis1.upper()       
                    if dis=="YES":
                        #Using exception handling to take correct input from the user
                        success=False
                        while success==False:
                            try:
                                discount=int(input("Enter discount amount="))
                                if discount<=list6[2] and discount>0:
                                    success=True
                                else:
                                    print("----------------------------------------------------------")
                                    print("Discount amount cannot be greater than the mentioned price")
                                    print("----------------------------------------------------------")
                            except:
                                print("---------------------------------------")
                                print("Please enter discount amount in numbers")
                                print("---------------------------------------")
                        s1=True
                        
                    elif dis=="NO":
                        discount=0
                        s1=True

                    else:
                        print("error")
                        s1=False
                  
                price=a*quantity
                finalprice=price-discount
                print("Discount amount=",discount)
                print("Total Price=",finalprice)
                name1=input("Enter your name=")
                name=name1.upper()
                
                #Using exception handling to take correct input from the user
                s2=False
                while s2==False:
                    try:
                        final=input("Do you really want to purchase this product(yes/no)=")
                        final_choice=final.upper()
                        if final_choice=="YES":
                            list6[1]=q
                            file()
                            print("Thank you for your purchase")
                            s2=True
                        elif final_choice=="NO":
                            print(Main.inventory(list5,list6,list7))
                            s2=True
                    except:
                        print("Error")
            else:
                print("----------------------")
                print("Currently not in stock")
                print("----------------------")
                
        elif choice=="LED":
            if list7[1]>0:
                success=False
                while success==False:
                    try:
                        quantity=int(input("Enter quantity="))
                        if quantity<=list7[1] and quantity>0:
                            success=True
                        else:
                            print("---------------------------------------------------------------")
                            print("Enter quantity is greater than or less than the available stock")
                            print("---------------------------------------------------------------")
                    except:
                        print("--------------------------------")
                        print("Please enter quantity in numbers")
                        print("--------------------------------")
                        
                print("Price=",list7[2])
                product=list6[1]
                q=product-quantity
                print("Quantity=",quantity)
                a=list7[2]   
                s1=False
                while s1==False:
                    dis1=input("Has discount been given(yes/no)?")
                    dis=dis1.upper()     
                    if dis=="YES":
                        #Using exception handling to take correct input from the user
                        success=False
                        while success==False:
                            try:
                                discount=int(input("Enter discount amount="))
                                if discount<=list7[2] and discount>0:
                                    success=True
                                else:
                                    print("-----------------------------------------------------------------------")
                                    print("Discount amount cannot be greater than or less than the mentioned price")
                                    print("-----------------------------------------------------------------------")
                            except:
                                print("---------------------------------------")
                                print("Please enter discount amount in numbers")
                                print("---------------------------------------")
                        s1=True
                        
                    elif dis=="NO":
                        discount=0
                        s1=True

                    else:
                        print("error")
                        s1=False
                  
                price=a*quantity
                finalprice=price-discount
                print("Discount amount=",discount)
                print("Total Price=",finalprice)
                name1=input("Enter your name=")
                name=name1.upper()

                s2=False
                while s2==False:
                    try:
                        final=input("Do you really want to purchase this product(yes/no)=")
                        final_choice=final.upper()
                        if final_choice=="YES":
                            list7[1]=q
                            file()
                            print("Thank you for your purchase")
                            s2=True
                        elif final_choice=="NO":
                            print(Main.invertory
                                  (list5,list6,list7))
                            s2=True
                    except:
                        print("Error")
            else:
                print("----------------------")
                print("Currently not in stock")
                print("----------------------")
                        
        else:
            print("-----------------------------------------------")
            print("NOT IN STOCK OR USER ENTERED WRONG PRODUCT NAME")
            print("-----------------------------------------------")
            
    elif run=="2" or run=="two":
        print(Main.inventory(list5,list6,list7))
            
    elif run=="3" or run=="three":
        a=",".join([str(i) for i in list5]) #Joins elemnts of list with" , "
        b=",".join([str(i) for i in list6]) #Joins elemnts of list with" , "
        c=",".join([str(i) for i in list7]) #Joins elemnts of list with" , "
        
        Test.read_file(a,b,c) #Calling a module to overwrite the main stock file
        break

    else:
        print("------------------------------")
        print("Please read the MENU carefully")
        print("------------------------------")





















    
