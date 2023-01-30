while True:
    user_action = input("type add or show, edit, complete, exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add' :
            todo = input("Enter a todo: ") + "\n"

            # file = open('files/todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            with open('todos.txt','r') as file:
                todos = file.readlines()

            todos.append(todo)

            # file = open('files/todos.txt','w')
            # file.writelines(todos)
            # file.close()

            with open('files/todos.txt','w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            # file = open('files/todos.txt','r')
            # todos = file.readlines()
            # file.close()

            with open('files/todos.txt','r') as file:
                todos =file.readlines()

            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
                row = f"{index+1}-{item}"
                print(row)

        case 'edit' : 
            number = int(input("Number of the dodo to edit: "))
            number = number - 1


            with open('files/todos.txt','r') as file:
                todos =file.readlines()
            

            new_todo = input("Enter new todo: ") 
            todos[number] = new_todo + '\n'

            print("here is how it will be", todos)
            
            with open('files/todos.txt','w') as file:
                file.writelines(todos)
            

        case 'complete':
            number = int(input("Number of the dodo to complete: "))

            with open('files/todos.txt','r') as file:
                todos =file.readlines()
            
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos.txt','w') as file:
                file.writelines(todos)
            
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        case 'exit' | 'q':
            break
        case whatever:
            print("Hey, you ented and unknown command")

print("bye!")
