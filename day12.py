# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)

# todos = [todo1, todo2, todo3, "hello"]

# print(todos)

# print(type(todo1))



# todos = []

# while True:
#     user_action = input ("type add or show: ")

#     match user_action:
#         case 'add' :
#             todo = input("Enter a todo: ")
#             todos.append(todo)
#         case 'show' :
#             print(todos)
#         case 'exit':
#             break

# print("bye!")


# todos = []

# while True:
#     user_action = input("type add or show: ")

#     match user_action:
#         case 'add' :
#             todo = input("Enter a todo: ")
#             todos.append(todo)
#         case 'show' :
#             for item in todos:
#                 print(item)
#         case 'exit':
#             break

# print("bye!")



todos = []

while True:
    user_action = input("type add or show, edit, complete: ")
    user_action = user_action.strip()

    match user_action:
        case 'add' :
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
                print(index, '-', item)
            print(f"Length is,{index + 1}")
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























