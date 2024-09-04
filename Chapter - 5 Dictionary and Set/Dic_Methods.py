marks = {'Professor':90,'Raimal':80,'Raja':70}
print(marks.items())#key vaue pair item we'll get inform of tupple

# keys() will return key values of dictionary
print(marks.keys())
#values() will return values of keys 
print(marks.values())

marks.update({"Mandha": "I love you"})
print(marks)

# upadate()will update dictionary, if already exist then it will update and if not then it will add
marks.update({"Professor":100})
print(marks)

# get() this method will return the value of key pair
print(marks.get("Professor"))#print none if not found
print(marks["Professor"])#return error if not found