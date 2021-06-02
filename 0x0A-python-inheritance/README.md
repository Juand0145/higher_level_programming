## Python - Inheritance
In this directory, we will find a compilation of files that will help us to understand and how to use inheritance in Python and help us to answer the next questions:

 -   What is a superclass, baseclass or parentclass
 -   What is a subclass
 -   How to list all attributes and methods of a class or instance
 -   When can an instance have new attributes
 -   How to inherit class from another
 -   How to define a class with multiple base classes
 -   What is the default class every class inherit from
 -   How to override a method or attribute inherited from the base class
 - -   Which attributes or methods are available by heritage to subclasses
 -   What is the purpose of inheritance
 -   What are, when and how to use  `isinstance`,  `issubclass`,  `type`  and  `super`  built-in functions 
## Files
 - 0-lookup.py is a function that returns the list of available attributes and methods of an object
 - 1-my_list.py, tests/1-my_list.txt is a class `MyList` that inherits from `list`
 - 2-is_same_class.py is a function that returns `True` if the object is _exactly_ an instance of the specified class ; otherwise `False`
 - 3-is_kind_of_class.py is a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.
 - 4-inherits_from.py is a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`
 - 5-base_geometry.py is an empty class `BaseGeometry`
 - 6-base_geometry.py is a class `BaseGeometry` (based on `5-base_geometry.py`).
 - 7-base_geometry.py, tests/7-base_geometry.txt is a class `BaseGeometry` (based on `6-base_geometry.py`).
 - 8-rectangle.py is a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).
 - 9-rectangle.py is a class  `Rectangle`  that inherits from  `BaseGeometry`  (`7-base_geometry.py`). (task based on  `8-rectangle.py`)
 - 10-square.py is a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):
 - 11-square.py is a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).
