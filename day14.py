# message = "corona vaccine is ready to use, most of them are more than 90% effective"
# print(message)
# print(message.capitalize())

# Message = message.capitalize()

# print(Message)
# """
# dir() function
# print(dir([]))

# """
# """
# print(message.upper())
# print(message.islower())

# print(message.find("ready"))
# print(message[18:24])


# seq1 = ("111","222")
# print(".".join(seq1))
# print("/".join(seq1))
# print("-".join(seq1))
# """
# """
# mountains = ["Everest", "Himalaya", "Alps", "K2"]

# mountains.append("Oregon mount") #add
# print(mountains)

# mountains.insert(1, "test") #add
# print(mountains)

# mountains.pop(5)
# print(mountains)
# """

# def vac_feedback(vac, efficacy):
#     print(f"{vac} vaccine is having {efficacy} % efficacy")

#     if(efficacy >50) and (efficacy <= 75):
#         print("Sure, good.")
#     elif(efficacy >75) and (efficacy <= 90):
#         print("Sure, good well.")
#     elif efficacy >=90:
#         print("Sure, will take the shot.")
#     else: 
#         print("Needs many more trials.")

# vac_feedback("Pfizer", 95)
# vac_feedback("3324", 45)


# def order_food(min_order, *args):
#     print(f"You have ordered : {min_order}")
# #    print(args)
#     for item in args:
#         print(f"You have ordered: {item}")

# order_food("Salad","Pizza")

import random


def time_activity(*args, **kwarrgs):
    print(args)
    print(kwarrgs)
    min = sum(args) + random.randint(0, 60)
    print(min)
    choice = random.choice(list(kwarrgs.keys()))
    print(choice)
time_activity(10,20,30, hobby = "dance", sport="boxing", fun="driving", work="devops")





















































