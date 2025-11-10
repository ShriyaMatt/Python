# Program to find the ASCII value of a given character

def get_ascii_value():
    char = input("Enter a single character: ")

    

    # Get ASCII value using ord()
    ascii_value = ord(char)
    print(f"The ASCII value of '{char}' is {ascii_value}")

if __name__ == "__main__":
    get_ascii_value()