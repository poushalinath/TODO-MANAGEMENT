help_text = "Welcome to todo-management /nPress 1 for seeing all the todo. /nPress 2 for adding a todo. /nPress 3 for deleting a todo."
choice = input(help_text + "\n> ")
if choice == "1":
    try:
        file = open("todo.txt", "r+")
    except:
        print("No todos exists at the moment.")
        exit()
    todos = file.read().split("\n")
    todos.remove('')
    if len(todos) == 0:
        print("No todos exists at the moment.")
        exit()
    for i in range(0, len(todos)):
        print(f"[{i + 1}] {todos[i]}")
    file.close()
elif choice == "2":
    todo = input("Enter the todo to add: ")
    file = open("todo.txt", "a")
    file.write(todo + "\n")
    file.close()
elif choice == "3":
    file = open("todo.txt", "r+")
    todos = file.read().split("\n")
    todos.remove('')
    for i in range(0, len(todos)):
        print(f"[{i + 1}] {todos[i]}")
    file.close()
    file = open("todo.txt", "w")
    todo_number = int(input("Enter the todo number to be deleted: "))
    todos.pop(todo_number - 1)
    for i in range(0, len(todos)):
        file.write(todos[i] + "\n")
    file.close()
else:
    print("That is not a valid option.")
    print(help_text)