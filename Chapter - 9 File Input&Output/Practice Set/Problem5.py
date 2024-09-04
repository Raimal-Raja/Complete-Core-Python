# Repeat program 4 for a list of such words to be censored
words = [ "Professor", "Raimal", "Raja"]
with open("myfile.txt", 'r') as f:
    content = f.read()
for word in words:
    content = content.replace(word, "*"*len(word))
    
with open("myfile.txt",'w') as f:
    f.write(content)