#  basic class

# class TestClass:
#     test_var = ('hello')
#     another_var = 'world'
#
#     def test_func(self):
#         print('function in a class')
#         print(self.test_var)
#         self.another_func('123')
#
#
#     def another_func(self, test_param):
#         print(test_param)


# create an instance
# test = TestClass()
# print(test.test_var)
# test.another_var = 'new value'
# print(test.another_var)
#
# test2 = TestClass()
# print(test2.another_var)
# test2.test_func()
# test2.another_func('test')

# mage class
# class Mage:
#     def __init__(self, health, mana):
#         self.health = health
#         self.mana = mana
#         print("the mage was created")
#         print(self.health, self.mana)

# def __len__(self):
#     return self.mana

# def attack(self, target):
#     target.health -= 10

# class Monster:
#     health = 40
#
#
# mage = Mage(100, 200)
# print(len(mage))
# monster = Monster()
#
# print(monster.health)
# mage.attack(monster)
# print(monster.health)


# inheritance

# class Human:
#
#     def __init__(self, health):
#         self.health = health
#
#     def attack(self):
#         print('attack')
#
#
# class Warrior(Human):
#     def __init__(self, health, defense):
#         super().__init__(health)
#         self.defense = defense
#
#
# class Barbarian(Human):
#     def __init__(self, health, damage):
#         self.damage = damage
#         super().__init__(health)
#
#
# warrior = Warrior(50, 5.5)
# barbarian = Barbarian(100, 8.1)
# warrior.attack()
# barbarian.attack()
# print(warrior.health)

# exercise

class Entity:

    def attack(self):
        print(f'attack with {self.damage} damage')


class Monster(Entity):

    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def __repr__(self):
        return f'a monster with {self.health} hp'


monster = Monster(100, 10)
print(monster.health)
monster.attack()

print(monster)
