# matrix = [
#     [1,2,3],
#     [2,4,6],
#     [7,8,9]
# ]


# print(f"this is {matrix}")
# ####################################
# basket = [1,6,2,3,4,5]
# # print(len(basket))

# # basket.extend([4,100])
# # new_list=basket 

# # # print(basket)
# # # print(new_list)
# # ####################################

# # #removing
# # basket.pop()
# # # print(basket)

# # new_sencense= ''.join(['hi','my','name'])

# # print(new_sencense)

# # print(basket[::-1])
# # print(basket)
# a,b,c = [1,2,3]
# basket = [1,2,3]

# print(a,b,c,basket)

# dictionary = {
#     'a' : 1,
#     'b' : 2,
#     'x' : True
# }

# # print(dictionary)


# dictionary = {
#     'weapons' : [1,2,3],
#     'greeting' : 'hello',
#     'is_Magic' : True
# }

# print(dictionary['weapons'])

# user = {
#     'basket':[1,2,3],
#     'greet': 'hello',
#     'age': 50
# }

# print(user.update({'ages':55}))



#Tuple
# my_tuple = (1,2,3,4,5)
# print( 5 in my_tuple)

# user = {
#     (1,2) : [1,2,3],
#     'greet' : 'hello',
#     'age' : 20
# }

# print(my_tuple)


my_tuple = (1,2,3,'fff4',5)
print(my_tuple.index(5))


my_set = {1,2,3,4,5,6}
your_set = my_set.copy()

print(my_set.difference(your_set))