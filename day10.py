#OOP
class PlayerCharacter: 
    # Class object attribute
    membership = True
    def __init__(self, name, age):
      if (PlayerCharacter.membership):
        self.name = name #attributes
        self.age = age
    
    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_thins2(num1, num2):
        return num1 + num2

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50 

print(player1.shout())
print(player2.shout())


