In this file
# Intermediate Python Topics

## 1. Optional Parameters

In Python, functions can have optional parameters, allowing you to provide default values for arguments. This gives flexibility when calling functions, as arguments with default values can be omitted.

Example:

```python
def greet(name, greeting='Hello'):
    print(f'{greeting}, {name}!')

greet('John')  # Output: Hello, John!
greet('Jane', 'Good morning')  # Output: Good morning, Jane!
```

## 2. staticmethod and classmethod

#### staticmethod
The staticmethod decorator is used to define a static method within a class. Static methods don't have access to class or instance-specific data.

Example:

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

result = MathOperations.add(5, 3)  # Result: 8
```

#### classmethod
The classmethod decorator is used to define a class method. Class methods take the class as the first argument, allowing access to class-level attributes.

Example:

```python
class MyClass:
    class_variable = 10

    @classmethod
    def print_class_variable(cls):
        print(cls.class_variable)

MyClass.print_class_variable()  # Output: 10
```

## 3. map Function
The map function applies a given function to all items in an iterable (e.g., a list) and returns an iterator of the results.

Example:

```python
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]
```

## 4. filter Function
The filter function is used to filter elements of an iterable based on a function that returns True or False.

Example:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]
```

## 5. lambda Function
A lambda function is an anonymous function defined using the lambda keyword. It is often used for short, simple operations.

Example:

```python
multiply = lambda x, y: x * y
result = multiply(3, 4)  # Result: 12
```

## 6. Collections in Python
Python provides several built-in collection types like lists, tuples, sets, and dictionaries. Additionally, the collections module offers specialized data structures like namedtuple, deque, Counter, and defaultdict.


# Code:
[HeHe.. Code here!!](https://github.com/Tejvil/PythonSkillBuilder.git)

