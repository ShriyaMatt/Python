#Take input of a word
string=input("Please enter your own word: ")
#take input of a character
char=input("Please enter your character: ")
i=0
count=0
#loop will find the occurence of a character
while(i< len(string)): #string operation

    if(string[i]==char): #condition 1
        count=count+1
    i=i+1

#Display the results
print("The whole number of times",char,"has occured =", count)