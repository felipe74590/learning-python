""" Create a ToDo App"""
# todos = []

while True:

    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.lower().strip()

    match user_action:
        case "add" :
            todo = input("Enter a todo item: ") + "\n"
            # assumes that the file already exits
            with open('text_files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('text_files/todos.txt', 'w') as file:
                file.writelines(todos)

        case "show" | "display" : #use a bitwise or OR operator
            with open('text_files/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}: {item.title()}"
                print(row)

        case "edit" :
            number = int(input("Number of the todo item to edit: "))
            update = input("Enter change: ")

            with open('text_files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos[number-1] = update + '\n'

            with open('text_files/todos.txt', 'w') as file:
                file.writelines(todos)

        case "complete":
            number = int(input("Number of the completed todo item: "))

            with open('text_files/todos.txt','r') as file:
                todos = file.readlines()

            completed_todo = todos[number-1].strip('\n').title()
            todos.pop(number-1)

            with open('text_files/todos.txt','w') as file:
                file.writelines(todos)

            message = f'Todo {completed_todo} was completed'
            print(message)

        case "exit":
            break
        
        case _:
            print("Hey, the command you entered is not available!")

print("Get to it!")
    