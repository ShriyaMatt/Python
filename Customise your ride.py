print("Select your ride:")
print("1.Bike")
print("2.Car")
choice=int(input("Enter Your Choice:"))
if(choice==1):
    print("What type of bike?")
    print("1.Scooty\n")
    print("2.Scooter\n")
    choice2=int(input("Enter your choice2:"))
    if choice2==1: # inner if statment
     print("You have selected scooty.")
    else:
      print("You have selected scooter.")


elif(choice==2): #outer elif statment
     print("What type of car?")
     print("1.Sudan")
     print("2.XUV")
     choice3=int(input("Enter your choice3:"))
     if choice3==1: #inner if statment
      print("You have selected Sudan.") 
     else:
      print("You have selected XUV. ")
else: #outer else statment
        print("Wrong Choice!")