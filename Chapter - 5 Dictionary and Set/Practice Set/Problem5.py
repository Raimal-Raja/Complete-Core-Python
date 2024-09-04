# create an empty dictionary. allow 4 friends to enter their
#  favorite languages as value and use key as their name. 
# assume that names are unique
dict = {}
name = input("Enter friend name: ")
lang = input("Enter your favorite lang: ")
dict.update({name:lang})
name = input("Enter friend name: ")
lang = input("Enter your favorite lang: ")
dict.update({name:lang})
name = input("Enter friend name: ")
lang = input("Enter your favorite lang: ")
dict.update({name:lang})
name = input("Enter friend name: ")
lang = input("Enter your favorite lang: ")
dict.update({name:lang})

print(dict)