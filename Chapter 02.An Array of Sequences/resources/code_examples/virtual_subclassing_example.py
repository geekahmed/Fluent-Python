"""
**The Traditional Inheritance Model**

Usually, when we talk about subclasses, we think of explicit inheritance:

```python
class Animal:  # Parent (Base) Class
    def speak(self):
        pass  # This method is inherited by subclasses

class Dog(Animal):  # Child (Derived) Class
    def speak(self):
        return "Woof!"
```

Here, `Dog` explicitly inherits from `Animal`.  This means it automatically gets all the attributes and methods defined in `Animal`, unless it overrides them.

**Virtual Subclasses (Duck Typing with a Twist)**

Python's flexibility allows for a different kind of subclassing called "virtual subclassing." This is where a class doesn't directly inherit from an abstract base class (ABC) but is still treated as if it did. 

Think of it like this:

* **Duck Typing:**  If it walks like a duck and quacks like a duck, it's a duck.  In Python, if your class provides the necessary methods and behaviors, it can be used in places where a specific type of object is expected, even without explicit inheritance.

* **Registering with ABCs:**  Virtual subclassing takes duck typing a step further. It allows you to formally tell Python, "Hey, even though my class doesn't directly inherit from this ABC, it *does* behave like it should, so treat it as a subclass."  This is done using the `register()` method of the ABC.

**Example with Sequences**

In Python, the `Sequence` and `MutableSequence` classes are abstract base classes (ABCs) that define common behaviors for sequence-like objects.  Built-in types like `list` and `tuple` were created before ABCs existed, so they don't directly inherit from them. However, they implement all the necessary methods to act like sequences.

To maintain consistency, Python uses virtual subclassing to bridge the gap.  This is why `issubclass(tuple, abc.Sequence)` returns `True` even though `tuple` doesn't explicitly inherit from `Sequence`.

**Why Use Virtual Subclasses?**

* **Backward Compatibility:**  It allows older classes to work seamlessly with newer code that relies on the abstract base class hierarchy.
* **Flexibility:** It lets you define classes that conform to an interface without being tied to a specific inheritance tree.

**Key Points to Remember**

* Virtual subclassing is a way to make a class act like a subclass of an ABC without direct inheritance.
* It leverages Python's duck typing philosophy.
* The `register()` method of the ABC is used to establish the virtual subclass relationship.

"""

from collections import abc

# Check if tuple is a sub class of Sequence (Immutable)
print(f'Is a tuple a sub class of sequence abc? {issubclass(tuple, abc.Sequence)}')

# Check if list is a sub class of MuttableSequence (mutable)
print(f'Is a list a sub class of mutable sequence abc? {issubclass(list, abc.MutableSequence)}')

# Check if string is a sub class of Sequence (Immutable)
print(f'Is a string a sub class of sequence abc? {issubclass(str, abc.Sequence)}')


# Example of using the register method
# Scenario:
"""
Imagine you have a custom class MySequence that you want to treat as a sequence, but it wasn't designed to directly inherit from the collections.abc.Sequence ABC.
"""

class MySequence:
    def __init__(self, data) -> None:
        self._data = data

    def __len__(self):
        return len(self._data)
    
    def __getitem__(self, index):
        return self._data[index]

# Register MySequence as a virtual subclass of Sequence
abc.Sequence.register(MySequence)

# Check if mysequence is a sub class of Sequence (Immutable)
print(f'Is a my sequence a sub class of sequence abc? {issubclass(MySequence, abc.Sequence)}')


# Testing the MySequence and use it like a real sequence
my_seq = MySequence([1, 2, 3])

# Use it like a sequence
print("The data inside my_seq object is: ")
for item in my_seq:
    print(item)  # Output: 1, 2, 3
