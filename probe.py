# class Wife:
#     """Простая модель любимой жены"""
#
#     def __int__(self, name, age, weight):
#         """Инициализирует атрибуты name и age."""
#         self.name = 'Marta'
#         self.age = age
#         self.weight = weight
#
#     def cooking(self):
#         """Метод по которому жена готовит"""
#         print(self.name.title() + ' is cooking now!')
#
#     def beautiful(self):
#         """Метод определяющий красоту по возрасту"""
#         if self.age < 40:
#             print(self.name.title() + ' is very beautiful!.')
#         else:
#             print(print(self.name.title() + " doesn't beautiful!."))
#
#     def healthy(self):
#         """Метод определяющий здоровье супруги"""
#         if self.weight > 55:
#             print(self.name.title() + " 's health is good!")
#         else:
#             print(self.name.title() + " 's health is not good!")

# class Dog():
#     """Простая модель собаки."""
#
#
# def __init__(self, name, age):
#     """Инициализирует атрибуты name и age."""
#
#
#     self.name = name
#     self.age = age
#
#
# def sit(self):
#     """Собака садится по команде."""
#     print(self.name.title() + " is now sitting.")
#
#     def roll_over(self):
#         """Собака перекатывается по команде."""
#
#     print(self.name.title() + " rolled over!")
#
# my_dog = Dog('Willie', 5)
# print(my_dog.sit())

import string


def pig_it(text):

    first_list = text.split()
    some_list = []
    cheking_list = list(string.punctuation)
    for str in first_list:
        some_list.append(str[1:] + str[0] + 'ay')
        new_string = ' '.join(some_list)

    return new_string

text = "Pig latin is cool"
print(pig_it(text))

#result = re.sub(r'[^\w\s]','', new_string[0:len(new_string) - 2])