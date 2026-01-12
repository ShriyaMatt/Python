start = int(input("Start: "))
end = int(input("End: "))

squares = [n**2 for n in range(start, end+1)]
print("Squares:", squares)
print("Even:", [x for x in squares if x % 2 == 0])
print("Odd:", [x for x in squares if x % 2 != 0])