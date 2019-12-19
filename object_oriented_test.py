# "object" in parenthesis below indicates what this class inherits from
class Human(object):
    '''
    Human has name and gender
    '''
    # Class level attribute
    # these codes will always execute when the class is instantiated
    planet = 'Earth'

    # I don't think it's good practice to use class level method though
    # You'd rather make it an independent function in the module
    @staticmethod
    def class_level_method():
        print('Class level method success!', end='\n\n')

    # Instance level attributes need instantiation
    def __init__(self, name, gender):
        # hiding attributes
        self.__name = name
        self.__gender = gender

    def info(self):
        print(f'My name is {self.__name} and I am a {self.__gender}.')

    # since the attribute is private, child class could not get the attributes
    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

def main():
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
        print('Fail to get private attributes')

    print('')
    print('Using class level method:')
    # so class level method can only be used on class level
    Human.class_level_method()

    me.info()


if __name__ == '__main__':
    main()
