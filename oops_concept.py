# oops_concepts.py: Learn Object-Oriented Programming (OOP) in Python

# 1. **Classes and Objects**
# In Python, OOP is based on the concept of classes and objects. A class is a blueprint for creating objects (a particular data structure), and an object is an instance of that class.

class Animal:
    # Constructor (__init__) is called when a new object is created from this class
    def __init__(self, name, species):
        self.name = name  # Instance variable
        self.species = species  # Instance variable
    
    # Method to print object details
    def speak(self):
        print(f"{self.name} the {self.species} is making a sound.")

# Create an object of Animal class
dog = Animal("Buddy", "Dog")
dog.speak()  # Output: Buddy the Dog is making a sound.

# 2. **Encapsulation**
# Encapsulation is the bundling of data (attributes) and the methods that operate on the data within a single unit or class.
# It also refers to restricting access to some of an object's components and only exposing the necessary parts.

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute
    
    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.__balance}")
        else:
            print("Deposit amount should be greater than zero.")
    
    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")
    
    # Method to check balance (getter for private variable)
    def get_balance(self):
        return self.__balance
    
    # Private method
    def __validate_account(self):
        print("Validating account...")

# Create an object of BankAccount
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Accessing private attribute via getter
# account.__balance  # This will raise an error because __balance is private

# 3. **Inheritance**
# Inheritance allows a class to inherit attributes and methods from another class. This helps in creating a new class using an existing class, enabling code reusability.

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call the constructor of the parent class
        self.breed = breed  # New attribute
    
    # Overriding the speak method
    def speak(self):
        print(f"{self.name} the {self.breed} barks!")

# Create an object of Dog class
dog1 = Dog("Rex", "German Shepherd")
dog1.speak()  # Output: Rex the German Shepherd barks!

# 4. **Polymorphism**
# Polymorphism allows methods to do different things based on the object it is acting upon. This is achieved through method overriding and method overloading.

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Cat")
        self.breed = breed

    def speak(self):
        print(f"{self.name} the {self.breed} meows!")

# Polymorphism example
def animal_speak(animal):
    animal.speak()  # Will call the correct speak method based on the object

# Create objects of different classes
cat = Cat("Whiskers", "Persian")
animal_speak(dog1)  # Output: Rex the German Shepherd barks!
animal_speak(cat)   # Output: Whiskers the Persian meows!

# 5. **Abstraction**
# Abstraction is the concept of hiding the complex implementation details of a system and exposing only the essential features to the user.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method, must be implemented by subclass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    # Implementing the abstract method
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    # Implementing the abstract method
    def area(self):
        return self.side * self.side

# Create objects of Circle and Square
circle = Circle(5)
square = Square(4)

print(f"Circle area: {circle.area()}")  # Output: Circle area: 78.5
print(f"Square area: {square.area()}")  # Output: Square area: 16

# 6. **Class and Static Methods**
# Class methods work with the class itself rather than instance objects, and static methods don't work with the class or the instance.

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def description(cls):
        return "This class provides basic math operations."

# Calling static method
print(MathOperations.add(5, 10))  # Output: 15

# Calling class method
print(MathOperations.description())  # Output: This class provides basic math operations.

# 7. **Private and Public Attributes/Methods**
# By convention, attributes prefixed with an underscore (e.g., _name) are considered 'protected' and not directly accessed outside the class.
# Attributes with double underscores (e.g., __name) are considered 'private' and are name-mangled to avoid accidental access.

class Student:
    def __init__(self, name, grade):
        self.name = name  # Public attribute
        self.__grade = grade  # Private attribute
    
    # Getter method for private attribute
    def get_grade(self):
        return self.__grade
    
    # Setter method for private attribute
    def set_grade(self, grade):
        self.__grade = grade

# Create an object of Student class
student = Student("John", "A")
print(student.name)  # Output: John (Public attribute)
print(student.get_grade())  # Output: A (Accessing private attribute via getter)
# print(student.__grade)  # Will raise an error as __grade is private

# 8. **Method Resolution Order (MRO)**
# Method Resolution Order defines the order in which classes are inherited when there is multiple inheritance.
class A:
    def hello(self):
        print("Hello from class A!")

class B(A):
    def hello(self):
        print("Hello from class B!")

class C(A):
    def hello(self):
        print("Hello from class C!")

class D(B, C):
    pass

# Method Resolution Order (MRO) for class D
d = D()
d.hello()  # Output: Hello from class B! (MRO is B -> C -> A)
print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

