def write_todos(todos, filepath='text_files/todos.txt'):
    """Update todos in todos file"""
    with open(filepath, 'w') as file:
        file.writelines(todos)

def read_todos(filepath='text_files/todos.txt'):
    """ Read todos from todo file"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

if __name__ == "__main__":
    print("Hello")
    print(read_todos())