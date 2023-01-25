# is_old  = False
# is_licenced = False

# if is_old: 
#     print('you are old enough to drive!')
# elif is_licenced:
#     print('you can drive now')
# else:
#     print('you are not of age')
# print('okok')


#Truthy and Falsy

# is_old = bool('hello')
# is_licensed = bool(5)

# print(is_old)
# print(is_licensed)

# password = '123'
# username = 'johnny'

# if password and username:
#     print('test it') 

# is_friend = False
# can_message = "message allowed" if is_friend else "not allowed to message"

# print(can_message)


# #Short Circuiting
# print('A'>'a')
# print(1<2>3<4)
# print(0 != 0)

# is_magicaian = True
# is_expert = True

# if is_expert and is_magicaian:
#     print("you are a mast magician")

# elif is_magicaian and not is_expert:
#     print("at least you're getting there")

# elif not is_magicaian:
#     print(" you need magic powers")


# for item in 'Zero to Mastery':
#     print(item)

# for item in [1,2,3,4,5]:
#     print(item)

 
# for item in (1,2,3,4,5,6):
#     for x in ['a','b','c']:
#         print(1,'c')


# #counter
# my_list = [1,2,3,4,5,6,67,78]
# counter = 0
# for item in my_list:
#     counter = counter + item
# print(counter)

# print(range(0, 100))


# for number in range(0, 10):
#     print('email email list')


# for _ in range(0, 10, 2):
# #     print(_)

# for char in enumerate('Hello'):
#     print(char)

# for i,char in enumerate(list(range(100))):
#     if char == 50:
#         print(f'indexP : {i}')

# i = 0
# while i < 1:
#     print(i)
#     i += 2
#     break
# else:
#     print("done with all the work")s


# for item in [1,2,3]:
#     print(item)
# i = 0
# while i < len([1,2,3]):
#     print(my_list[i])
#     break

# while True:
#     input('say somethin:')
#     break

# while True:
#     response = input('say something: ')
#     if(response == 'bye'):
#         break

# # DRY
# def say_hello():
#     print('helooo')

# say_hello()
# say_hello()

# #parameters
# def say_hello(name, emoji):
#     print(f'heeeoooo {name} {emoji}')

# #arguments
# say_hello('Andrei', '＠')
# say_hello('Ryan', '＠')
# say_hello('Andy', '＠')


# #positional arguments 
# say_hello('＠','Test')

# #keyword arguments
# say_hello(emoji='＠', name='bibi')



# def sum(num1, num2):
#     return num1 + num2
# print(sum(4,5))


# def sum(num1, num2):
#     def another_func(n1,n2):
#         return n1+n2
#     return another_func(num1, num2)

# total = sum(10, 20)
# print(total)




# def test(a):
#     '''
#     Info: this function test 
#     '''
#     print(a)

# test('!!!!')
# print(test.__doc__)


# # clean code
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False

# print(is_even(51))


# def super_func(*args):
#     print(*args)
#     return sum(args)
# super_func(1,2,3,4,5)

# def highest_even(li):
#     evens = []
#     for item in li:
#         if item % 2 == 0:
#             evens.append(item)
#     return max(evens)

# print(highest_even([1,2,3,4,8]))

# a = 'helloooo'
# if ((n := len(a))>10):
#     print(f"too long {len(a)} elements")

 

# a = 1

# def confusion():
#     a = 5
#     return a
# print(a)
# print(confusion())


# total = 0
# def count():
#     global total
#     total += 1
#     return total
# count(total)

# print(count())