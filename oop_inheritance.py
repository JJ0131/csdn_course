from object_oriented_test import Human


class Student(Human):
    def __init__(self, name, gender, grade):
        # use parent class's init method
        Human.__init__(self, name, gender)
        self.__grade = grade

    def info(self):
        try:
            print(f'My name is {self.__name}, I am a {self.__gender}, my grade is {self.__grade}')
        except AttributeError:
            print('Could not access parent class private attributes',end='\n\n')

        print(f'My name is {self.get_name()}, I am a {self.get_gender()}, my grade is {self.__grade}')


def main():
    stu = Student('abc', 'Male', '99')
    stu.info()


if __name__ == '__main__':
    main()
