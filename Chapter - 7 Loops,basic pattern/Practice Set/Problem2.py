'''write a program to great all the person
names stored in a list and which starts with S'''
l = ['Professor', 'Raimal','Raja']

for name in l:
    if(name.startswith("R")):
        print(f"Hello gentle man! {name} ")
    else:
        print("Hello Professor! ")