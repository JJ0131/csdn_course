# "object" in parenthesis below indicates what this class inherits from
class Human(object):
    '''
    Human has name and gender
    '''
    # Class level attribute
    planet = 'Earth'
    print('Can I print something in class definition?')

    def class_level_method():
        print('Can I use class level method?', end='\n\n')

    # Instance level attributes need instantiation
    def __init__(self, name, gender):
        # hiding attributes
        self.__name = name
        self.__gender = gender

    def show_yourself(self):
        print(f'My name is {self.__name} and I am a {self.__gender}.')


print('Class level attribute:')
print('this human lives on ', Human.planet, '.')
print('')

print('Try printing Human.name:')
try:
    print(Human.__name)
except AttributeError:
    print('Here is an error - you need instantiation to use instance level attribute')

print('')
print('Printing instance attributes')
me = Human('Jian Jin', 'male')
try:
    print('Trying to get private attributes.')
    print(f"This human's name is {me.__name} and he is a {me.__gender}.")
except AttributeError:
    print('Yep. No private attribute for you!')

print('')
print('Using class level method:')
# so class level method can only be used on class level
Human.class_level_method()

me.show_yourself()
