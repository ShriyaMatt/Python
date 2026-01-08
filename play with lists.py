L=[4,5,1,2,9,7,10,8]
print("Orginal List:",L)

#varaiable to store the sum of
#the list
count=0

#finding the sum
for i in L:
    count += i

#didvide the total elements by
#number of elements
avg=count/len(L)

print("Sum=",count)
print("Average=",avg)

#sorting the elements of the list
print("Smallest element is:",L[0])

#printing the last element
print("Largest element is:",L[-1])