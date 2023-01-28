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


todos = []

while True:
    user_action = input("type add or show: ")

    match user_action:
        case 'add' :
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' :
            for item in todos:
                print(item)
        case 'exit':
            break

print("bye!")























