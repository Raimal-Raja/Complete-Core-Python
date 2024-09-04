# will be appended in last of file current data, as many time you run it will be appended again and again

st = "  Error spoted ..... this text will be appended ? "
f = open("myfile.txt", "a")

f.write(st)
f.close
f = open("myfile.txt")
data = f.read()
print(data)
