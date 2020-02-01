# Use the __str__ and __repr__ magic methods on your class to specify what an object's string representation should be. It's just like the toString() method in JavaScript.

# If you print a Student object. The output would look something like below.

# mike = Student()
# mike.first_name = "Mike"
# mike.last_name = "Ellis"
# mike.age = 35
# mike.cohort_number = 39

# print(mike)
# <__main__.Student object at 0x107133f60>
# But if you specify exactly what string should be returned from __str__ or __repr__, that will print out instead. If you implement the following method on your class...

# class Student:

#     def __str__(self):
#         return f"{self.full_name}"
# then the output will change

# print(mike)
# Mike Ellis
# Change your class so that any objects created from it will be rerpesented as strings in the following format.

# Mike Ellis is 35 years old and is in cohort 39 


class Student:
    def __str__(self):
        return f'{self.full_name} is {self.age} and is in cohort {self.cohort_number}'
    
     # def first_name is a function that can be accessed as a property because of the @decorater
    @property
    def first_name(self):
        try:
            return self.__first_name
        # .__first_name is private: it's only available for changing inside this class
        except AttributeError:
            return ""

    @first_name.setter
    def first_name(self, first_name):
        if type(first_name) is str:
            # we are enforcing type rules here. checking for the type- it should be a string here.
            self.__first_name = first_name
        else:
            raise TypeError('Please provide first name as a string. NO NUMBERS ALLOWED I HATE MATH')

    @property
    def last_name(self):
        try:
            return self.__last_name
        # .__first_name is private: it's only available for changing inside this class
        except AttributeError:
            return ""

    @last_name.setter
    def last_name(self, last_name):
        if type(last_name) is str:
            # we are enforcing type rules here. checking for the type- it should be a string here.
            self.__last_name = last_name
        else:
            raise TypeError('Please provide last name as a string. NO NUMBERS ALLOWED I HATE MATH')


    @property
    def age(self):
        try:
            return self.__age
        # .__first_name is private: it's only available for changing inside this class
        except AttributeError:
            return 0

    @age.setter
    def age(self, age):
        if type(age) is int:
            # we are enforcing type rules here. checking for the type- it should be a string here.
            self.__age = age
        else:
            raise TypeError('Please provide age as a number. BUT I STILL HATE MATH')
    @property
    def cohort_number(self):
        try:
            return self.__cohort_number
        # .__first_name is private: it's only available for changing inside this class
        except AttributeError:
            return 0

    @cohort_number.setter
    def cohort_number(self, cohort_number):
        if type(cohort_number) is int:
            # we are enforcing type rules here. checking for the type- it should be a string here.
            self.__cohort_number = cohort_number
        else:
            raise TypeError('Please provide cohort # as a number. BUT I STILL HATE MATH')


    @property
    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'

# this is only one instance,, you just changed the name form shawna eddy
student = Student()
student.first_name = "Shawna"
student.last_name = "Honkey"
print(student.full_name)

student.first_name = "Eddy"
student.last_name = "Not a Honkey"
print(student.full_name)

student.age = 213
print(student.age)

student.cohort_number = 98
print(student.cohort_number)
print(student)
