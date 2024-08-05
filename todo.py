""" Create a ToDo App"""
# todos = []

def write_todos(todos, filepath='text_files/todos.txt'):
    """Update todos in todos file"""
    with open(filepath, 'w') as file:
        file.writelines(todos)

def read_todos(filepath='text_files/todos.txt'):
    """ Read todos from todo files"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos
    
while True:

    user_action = input(
    """ Type commands add 'insert todo here', show, edit 'insert item #', complete, or exit: """
    )
    user_action = user_action.lower().strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:] + '\n'

        # assumes that the file already exits
        todos = read_todos()
        todos.append(todo)
        write_todos(todos)

    elif user_action.startswith('show'): #use a bitwise or OR operator
        todos = read_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}: {item.title()}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            todos = read_todos()

            update = input("Enter change: ")
            todos[number-1] = update + '\n'

            write_todos(todos)
        except ValueError as err:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            # number = int(input("Number of the completed todo item: "))

            todos = read_todos()

            completed_todo = todos[number-1].strip('\n').title()
            todos.pop(number-1)

            write_todos(todos)

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
    