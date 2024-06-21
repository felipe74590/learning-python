""" Create a ToDo App"""
todos = []

while True:

    user_action = input("Type add, show, or exit: ")
    user_action = user_action.lower().strip()
    match user_action:
        case "add" :
            todo = input("Enter a todo item: ")
            todos.append(todo)
        case "show" | "display" : #use a bitwise or OR operator
            for item in todos:
                item = item.title()
                print(item)
        case "exit":
            break
        case _:
            print("Hey, the command you entered is not available!")

print("Get to it!")
    
    
