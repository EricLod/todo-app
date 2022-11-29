import webbrowser

user_term = input("Enter a search term: ").replace(" ", "+")

print(user_term)

webbrowser.open("https://www.google.com/search?q=" + user_term) #https://www.google.com/search?q=python+website

