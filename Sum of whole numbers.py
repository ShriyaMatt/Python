#Program to print whole number using for loop

n=int(input("Enter how many whole numbers you want:"))
sum=0
for i in range(1, n+1):
  sum=sum+i
  print("Sum of whole numbers is:", sum)