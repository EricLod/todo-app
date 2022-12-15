from modules import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text("", key="clock")
label = sg.Text("Hello World")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layoutStyle = [[clock],
               [label],
               [input_box, add_button],
               [list_box, edit_button, complete_button],
               [exit_button]]

window = sg.Window("My To-Do App",
                   layout=layoutStyle,
                   font=("Helvetica", 20))

while True:

    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values["todo"])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                print(4, todo_to_edit)
                new_todo = values["todo"]
                print(5, new_todo)
                todos = functions.get_todos()
                print(6, todos)
                index = todos.index(todo_to_edit)
                print(7, index)
                todos[index] = new_todo + "\n"
                print(todos)
                functions.write_todos(todos)
                window["todos"].update(values=todos)

            except IndexError:
                sg.popup_error("Please select an item first.", font=("helvetica", 50))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todo"].update("")
                window["todos"].update(todos)

            except IndexError:
                sg.popup_error("Please select an item first.", font=("Comic Sans", 50))

        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break
            
window.close()