# class PlayerCharacter:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def run(self):
#         return self
#     def speak(self):
#         print(f'my name is {self.name} and my age {self.age}')
# player1 = PlayerCharacter('andrei',100)
# print(player1.speak())
# print(len((1,2,3,1)))
# player1.speak()

# player1.name = '!!!'
# player1.speak = 'booo'

# print(player1.speak)

#Users
class User:
    def sign_in(self):
        print('logged in')
    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with power of {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)

print(isinstance(wizard1, User))

wizard1 = Wizard('Merlin', 50)
archer1 = Wizard('Robin', 50)
archer1 = Archer('Robin',30)
print(wizard1.attack())
wizard1.attack()
archer1.attack()

def player_attack(char):
    char.attack()
player_attack(wizard1)

print(wizard1.attack())















