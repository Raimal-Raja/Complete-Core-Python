#write a program to find out the line
# number where python is present from que -6
with open("Log.txt", 'r') as f:
    lines = f.readlines()
line_no = 1
for line in lines:
    if("python" in line):
        print(f"Python is present in line no {line_no}")
        break
    line_no+=1
    
else:
    print("python not found")