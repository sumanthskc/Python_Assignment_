# . Define a class Person and its two child classes: Male and Female. All classes have a 
# method "get_gender" which can print "Male" for Male class and "Female" for Female 
# Class. 
# Bonus: Make class Person an abstract class and make get_gender an abstract method in the 
# same class. The two child classes must inherit and implement get_gender. i.,e, When trying to 
# initialize an object of class Person, the program must throw an error. 
# Hint:  
# Use abc library (comes natively with Python3) https://www.python
# course.eu/python3_abstract_classes.php 

from abc import ABC, abstractmethod
class Person:
    @abstractmethod
    def get_gender(self):
        pass
class Male(Person):
    def get_gender(self):
        return "Male"
class Female(Person):
    def get_gender(self):
        return "Female"
m=Male()
f=Female()

print(f"{m.get_gender()}  ")
print(f"{f.get_gender()}")