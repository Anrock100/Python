user_input = input("Enter a string: ")

# reverse the user input using slicing
reversed_input = user_input[::-1]

# check if the user input and reversed input are equal
if user_input == reversed_input:
    print(user_input, "is a palindrome.")
else:
    print(user_input, "is not a palindrome.")
