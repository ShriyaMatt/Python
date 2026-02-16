class Reverse:
    def __init__(self, text="Hello World"):
        self.text = text

    def reverse_words(self):
        return " ".join(self.text.split()[::-1])


# Take input from user
user_input = input("Enter a string: ")

# Create object with user input or default
rev = Reverse(user_input if user_input else "Hello World")

# Print reversed string
print(rev.reverse_words())