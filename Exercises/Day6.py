file = open(r"C:\Users\eric\Downloads\essay.txt", 'r')
content = file.read()
print(content.title())

print(len(content))

name = "\n" + input("Add a new member: ") + "\n"

file = open(r"C:\Users\eric\Downloads\members.txt", 'r')
members = file.read()
print(members)
file.close()
file = open(r"C:\Users\eric\Downloads\members.txt", 'w')
members = str(members) + str(name)
file.write(members)
file.close()
print(members)
