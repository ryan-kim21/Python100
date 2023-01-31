while True:
    user_action = input("type add or show, edit, complete, exit: ")
    user_action = user_action.strip()

# match user_action:
    if 'add' in user_action:
        todo = user_action[4:]  #4칸 뒤 부터 입력

        with open('todos.txt','r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('files/todos.txt','w') as file:
            file.writelines(todos)



    elif 'show' in user_action:

        with open('files/todos.txt','r') as file:
            todos =file.readlines()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index+1}-{item}"
            print(row)


    elif 'edit' in user_action:

        number = int(user_action[5:])
        number = number - 1


        with open('files/todos.txt','r') as file:
            todos =file.readlines()
        

        new_todo = input("Enter new todo: ") 
        todos[number] = new_todo + '\n'

        print("here is how it will be", todos)
        
        with open('files/todos.txt','w') as file:
            file.writelines(todos)
        

    elif 'complete' in user_action:

        number = int(user_action[9:])

        with open('files/todos.txt','r') as file:
            todos =file.readlines()
        
        index = number -1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('files/todos.txt','w') as file:
            file.writelines(todos)
        
        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)

    elif 'exit' in user_action:
        break

    elif 'whatever' in user_action:
        print("Hey, you ented and unknown command")
    else:
        print("Command is nodt valid.")
    
print("bye!")
