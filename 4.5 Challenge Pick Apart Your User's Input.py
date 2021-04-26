##Write a script named first_letter.py that first prompts the user for
##input by using the string "Tell me your password:" The script should
##then determine the first letter of the user’s input, convert that letter
##to upper-case, and display it back.

user_input = input("Tell me your password: ")
user_input = user_input.strip()
first_letter_of_password = user_input[0]
print("Altered password is:", first_letter_of_password.upper() + user_input[1:])
