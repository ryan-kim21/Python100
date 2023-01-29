# waiting_list = ["sen","ben","john"]
# waiting_list = waiting_list.sort()

# for index, item in enumerate(waiting_list):
#     row = f"{index + 1}.{item.capitalize()}"
#     print(row)

while True:
    user_action = input("type add or show, edit, complete, exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add' :
            todo = input("Enter a todo: ") + "\n"

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('files/todos.txt','w')
            file.writelines(todos)
            file.close()

        case 'show' | 'display':
            file = open('files/todos.txt','r')
            todos = file.readlines()
            file.close()

            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
                row = f"{index+1}-{item}"
                print(row)

        case 'edit' : 
            number = int(input("Number of the dodo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ") 
            todos[number] = new_todo
            print(new_todo)

        case 'complete':
            number = int(input("Number of the dodo to complete: "))
            todos.pop(number - 1)

        case 'exit' | 'q':
            break
        case whatever:
            print("Hey, you ented and unknown command")

print("bye!")
