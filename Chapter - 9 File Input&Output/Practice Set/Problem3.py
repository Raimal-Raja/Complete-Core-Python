''' write a program to generate mutliplication tables
2 to 20 and write it to the different files. 
Place these files in a folder ofr a 13 years old'''

def generateTable(n):
    table =''
    for i in range(1 ,11):
        table += f"{n} X {i} = {n*i}\n"
    with  open(f"Tables/table_{n}.txt", "w") as f:
        f.write(table)
for i in range(2,21):
    generateTable(i)