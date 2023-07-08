#How to greate a Strong Password in Python
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
# select randomly chars from letters list
# password = ""
# for char in range(1, nr_letters+1):
#     password +=  random.choice(letters)

# # select randomly symbols from symbols list
# for symbl in range(1, nr_symbols+1):
#     password +=  random.choice(symbols)

# # select randomly numbers from numbers list
# for num in range(1, nr_numbers+1):
#     password +=  random.choice(numbers)

# #string_password = ''.join(final_list)
# #
# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password =[]
for char in range(1, nr_letters+1):
    password +=  random.choice(letters)

# select randomly symbols from symbols list
for symbl in range(1, nr_symbols+1):
    password +=  random.choice(symbols)

# select randomly numbers from numbers list
for num in range(1, nr_numbers+1):
    password +=  random.choice(numbers)

print(password)
#Shuffle_Password
random.shuffle(password)
print(password)
# change the list to String
# string_password = ''.join(password)

# better way to Convert  a List to String
string_password = ""
for char in password:
    string_password += char


print(string_password)
