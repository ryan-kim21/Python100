# #String
# print("test")
# print("123"+ "345")

# #Interger
# print(123+345)
# 123456789

# #Float
# 3.1234

# #Boolean
# True or False

# #type error
# #num_char = len(input("What is your name?"))
# #print("Your name has " + num_char + "characters.")

# #
# num_char = len(input("What is your name?"))
# #print("Your name has " + num_char + "characters.")
# print(type(num_char))



# a = 123
# print(type(a))


# print(70 + float("100.5"))

####################################
# two_digit_number = input("type a two digit>?")
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]

# result = int(first_digit) + int (second_digit)
# print(result)



####################################
# height = input ("enter your hight in m :")
# weight = input ("enter your weight in kg: ")

# bmi = int(weight)  / float(height) ** 2 
# bmi_as_int = int(bmi)
# print(bmi)
####################################

print("Welcome to the tip calculator.")
bill = float(input("what was the total bill?$"))
tip = int(input("Hw much tip would you like to give? 10, 12 or 15"))
people = int (input("How many people to split the bill?"))
tip_as_percent = tip /100
total_tip_amount= bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill /people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")



####################################  

####################################

####################################

####################################

####################################

####################################

####################################

####################################

####################################





####################################







































