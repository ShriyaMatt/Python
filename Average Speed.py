s1=int(input("Enter your first speed:"))
s2=int(input("Enter your second speed:"))
s3=int(input("Enter your third speed:"))
average=(s1+s2+s3)/3
print("The average speed is:", average)
if s1<average:
 print("Speed one is slower than the average with the speed of",average-s1)
if s2<average:
 print("Speed two is slower than the average with the speed of",average-s2)
if s3<average:
 print("Speed three is slower than the average with the speed of",average-s3)
 