import re

f = open("inputfile.txt", 'a')
f.close()

f = open("inputfile.txt", "r")
content = f.read()
f.close()

search = input("Enter search word: ")
replace = input("Enter replace word: ")

update, count = re.subn(search, replace, content, flags = re.IGNORECASE)

f = open("inputfile.txt", 'w')
f.write(update)
f.close()

if count > 0:
    print(f"Search and replace done {count} replacements done")
else:
    print("search word not found")

print("The updated content is : \n")   
f = open("inputfile.txt", 'r')
print(f.read())
f.close()