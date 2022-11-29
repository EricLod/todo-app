#from functions import get_todos, write_todos
from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is: ", now)

while True:
    user_action = input('Tye add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith("add"):
        try:
            todo = user_action[4:]
            if todo == "":
                todo = input('Enter a todo: ')
            todos = functions.get_todos()
            todos.append(todo + "\n")
            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f'{index + 1}-{item}'
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = user_action[5:]
            if number == "":
                number = input('Number of the todo to edit: ')
            number = int(number) - 1
            todos = functions.get_todos()
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + "\n"
            functions.write_todos(todos)

        except ValueError:
            print("")
            continue

    elif user_action.startswith("complete"):
        try:
            number = user_action[9:]
            if number == "":
                number = input("Number of the todo to complete: ")

            number = int(number)
            todos = functions.get_todos()
            index = number - 1
            todoRemoved = todos[index].strip("\n")
            todos.pop(index)
            message = f'Todo "{todoRemoved}" was removed from the list.'
            functions.write_todos(todos)
            print(message)

        except ValueError:
            print("")
            continue

    elif user_action.startswith("exit"):

        print("Cheers!")
        break

    else:

        print("No valid input.")
        print("Try again.")

print("Bye!")