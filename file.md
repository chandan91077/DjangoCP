# 🧠 OOPS (Object-Oriented Programming System)

**OOPS** is a programming approach where software is designed using **classes and objects** to model real-world entities.

---

## 🔹 Class & Object

* **Class** → Blueprint for creating objects
* **Object** → Instance of a class

### Example

```python
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

s1 = Student("Chandan")
s1.show()
```

---

## 🔹 Encapsulation

**Definition:** Binding data and methods together in a single unit (class).

### Example

```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print(self.balance)
```

---

## 🔹 Abstraction

**Definition:** Hiding implementation details and showing only essential features.

### Example

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts")
```

---

## 🔹 Inheritance

**Definition:** One class acquires properties and methods of another class.

### Example

```python
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    pass

Child().show()
```

---

## 🔹 Polymorphism

**Definition:** Same method name, different behavior.

### Example

```python
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

for a in (Dog(), Cat()):
    a.sound()
```

---

## ✅ One-Line Summary

> **OOPS uses classes and objects to structure programs using encapsulation, abstraction, inheritance, and polymorphism for better code reusability and maintainability.**

---

## 📌 Quick Revision (E-A-I-P)

* **E** → Encapsulation
* **A** → Abstraction
* **I** → Inheritance
* **P** → Polymorphism

---

##Decorator ?
A decorator is a function that takes another function as input and returns a new function with extended behavior.
```def my_decorator(func):
        def wrapper():
            print("Before function call")
            func()
            print("After function call")
        return wrapper
        
    
        @my_decorator
        def say_hello():
            print("Hello")
        say_hello()
```
## output
Before function call
Hello
After function call
