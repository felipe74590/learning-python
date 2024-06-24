""" Create a ToDo App"""
todos = []

while True:

    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.lower().strip()
    match user_action:
        case "add" :
            todo = input("Enter a todo item: ")
            todos.append(todo)
        case "show" | "display" : #use a bitwise or OR operator
            for index, item in enumerate(todos):
                row = f"{index+1}: {item.title()}"
                print(row)
        case "edit" :
            number = int(input("Number of the todo item to edit: "))
            update = input("Enter change: ")
            todos[number-1] = update
        case "complete":
            number = int(input("Number of the completed todo item: "))
            todos.pop(number-1)
        case "exit":
            break
        case _:
            print("Hey, the command you entered is not available!")

print("Get to it!")
    