""" Create a ToDo App"""
# todos = []

while True:

    user_action = input(
        """ Type commands add 'insert todo here', show, edit 'insert item #', complete, or exit: """
    )
    user_action = user_action.lower().strip()

    if "add" in user_action or 'new' in user_action:
        todo = user_action[4:] + '\n'

        # assumes that the file already exits
        with open('text_files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('text_files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif "show" in user_action: #use a bitwise or OR operator
        with open('text_files/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}: {item.title()}"
            print(row)

    elif "edit" in user_action:
        number = int(user_action[5:])
        print(number)

        with open('text_files/todos.txt', 'r') as file:
            todos = file.readlines()

        update = input("Enter change: ")
        todos[number-1] = update + '\n'

        with open('text_files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif "complete" in user_action:
        number = int(user_action[9:])
        # number = int(input("Number of the completed todo item: "))

        with open('text_files/todos.txt','r') as file:
            todos = file.readlines()

        completed_todo = todos[number-1].strip('\n').title()
        todos.pop(number-1)

        with open('text_files/todos.txt','w') as file:
            file.writelines(todos)

        message = f'Todo {completed_todo} was completed'
        print(message)

    elif "exit" in user_action:
        break
    
    else:
        print("Hey, the command you entered is not available!")

print("Get to it!")
    