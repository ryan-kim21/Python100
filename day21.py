def get_todos():
    with open('todos.txt','r') as file:
        todos = file.readlines()

    return todos





while True:
    user_action = input("type add or show, edit, complete, exit: ")
    user_action = user_action.strip()

# match user_action:
    if user_action.startswith("add"):
        todo = user_action[4:]  #4칸 뒤 부터 입력

        todos = get_todos()

        with open('todos.txt','r') as file:
            todos = file.readlines()

        todos.append(todo+'\n')

        with open('files/todos.txt','w') as file:
            file.writelines(todos)



    elif user_action.startswith("show"):

        todos = get_todos()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index+1}-{item}"
            print(row)


    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

    
            todos = get_todos()
            
            new_todo = input("Enter new todo: ") 
            todos[number] = new_todo + '\n'

            print("here is how it will be", todos)
            
            with open('files/todos.txt','w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
            # user_action = input("type add or show, edit, complete, exit: ")
            # user_action = user_action.strip()
            

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos.txt','w') as file:
                file.writelines(todos)
            
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")

    elif user_action.startswith("exit"):
        break

    elif 'whatever' in user_action:
        print("Hey, you ented and unknown command")
    else:
        print("Command is nodt valid.")
    
print("bye!")
