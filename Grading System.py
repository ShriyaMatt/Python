print("Enter the mark for five subjects:")
sub1=float(input("Subject 1 : "))
sub2=float(input("Subject 2 : "))
sub3=float(input("Subject 3 : "))
sub4=float(input("Subject 4 : "))
sub5=float(input("Subject 5 : "))
#Calculate total and average
total=sub1+sub2+sub3+sub4+sub5
average=total/5

#Determine Grade
if average>=90:
    grade="A+"
elif average>=80:
    grade="A"
elif average>=70:
    grade="B"
elif average>=60:
    grade="C"
elif average>=50:
    grade="D"
else:
    grade="F"

#Display Results
print("\n-----RESULT-----")
print(f"Total Marks-{total}")
print(f"Average={average:.2f}%")
print(f"Grade={grade}")