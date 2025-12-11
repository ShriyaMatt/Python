#Take user input
rows=int(input("Please enter the total number of rows:"))
number=1 #initalise by 1

print("Floyd's Triangle")
#outer loop for number of rows
for i in range (1, rows+1):
    #inner loop for number of colums
     for j in range(1,i+1):
        #Display result
         print(number,end='')
         number=number+1
     print()