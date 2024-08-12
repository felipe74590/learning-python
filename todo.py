import functions

""" Create a ToDo App"""

while True:

    user_action = input(
    """ Type commands add 'insert todo here', show, edit 'insert item #', complete, or exit: """
    )
    user_action = user_action.lower().strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:] + '\n'

        # assumes that the file already exits
        todos = functions.read_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith('show'): #use a bitwise or OR operator
        todos = functions.read_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}: {item.title()}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            todos = functions.read_todos()

            update = input("Enter change: ")
            todos[number-1] = update + '\n'

            functions.write_todos(todos)
        except ValueError as err:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            # number = int(input("Number of the completed todo item: "))

            todos = functions.read_todos()

            completed_todo = todos[number-1].strip('\n').title()
            todos.pop(number-1)

            functions.write_todos(todos)

            message = f'Todo {completed_todo} was completed'
            print(message)
        except IndexError:
            print(f"There is no #{number} todo does not exist.")
            continue

    elif "exit" in user_action:
        break
    
    else:
        print("Hey, the command you entered is not available!")

print("Get to it!")
    