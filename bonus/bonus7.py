filenames = ["1.doc", "1.report", "1.pesentation"]
filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print(filenames)

names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)

usernames = ["john 1990", "alberta1970", "magnola2000"]
usernames = [len(username) for username in usernames]
print(usernames)

user_entries = ['10', '19.1', '20']
user_entries = [float(user) for user in user_entries]
print(user_entries)

user_entries = sum(user_entries)
print(user_entries)