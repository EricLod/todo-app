password = input("Enter new password: ")
results = {}

if len(password) >= 8:
    results["length"] = True
else:
    results["length"] = False

results["digits"] = False
for i in password:
    if i.isdigit():
        results["digits"] = True

results["uppercase"] = False
for i in password:
    if i.isupper():
        results["uppercase"] = True

if all(results.values()):
    print("Password is strong.")
else:
    print("Password is weak.")

