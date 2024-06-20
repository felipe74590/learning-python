""" Create a ToDo App"""

user_prompt = "Enter a todo:"
todos = []
make_list = True
while make_list == True:
    todo = input(user_prompt)
    if todo.lower() == "done":
        print(f"my Todo list: {todos}")
        make_list = False
    else:
        todos.append(todo)
        print("Next... ")
    print(todo)
    
    
