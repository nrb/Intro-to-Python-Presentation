History of Python
=================
Developed by Guido von Rossum in 1989 at CWI
	 * CWI is a research institution funded by the Dutch government
	 * Guido needed something that was faster for development than C, less tied to Unix then Perl and bash.

Who uses Python?
================
* Google (Guido works there)
* DemonWare (Call of Duty servers)
* CCP Games (EVE Online)
* CRC (web development, scientific libraries)
* Dropbox
* Canonical (creators of Ubuntu)

What is Python?
===============
* An object-oriented, dynamically typed, interpreted, general purpose programming language

* Open source, BSD-like license

* Supported on lots of platforms

General Purpose
===============
Used for lots of different programming tasks
	* Automatic repetitive administrative tasks
	* Scientific calculations (libraries like SciPy and NumPy)
	* Web development (Django, Pyramid, Flask, Google App Engine, so on and so forth)
	
Interpreted
===========
Python code is translated to machine code at runtime, not in a prior compilation step.

Several interpreters
	* Standard CPython
	* PyPy project
	* Stackless

Dynamically Typed
=================
* Languages like Chapel, C, Java require variables to have their type declared on creation
* Python does not; a variable can hold any kind of value.

Examples::

	a = "a string"
	a = 1

Dynamically Typed
=================
* Variable's *properties* are important, not it's data type.
* Also known as "duck typing".
	* "If it walks like a duck and quacks like a duck, it's a duck".

Object-Oriented
===============
* Data and the functions related to it is associated through objects
* Objects are instances classes.
* More on this later.


Data Types
==========
* Several generic, basic data types:
        * Integers
        * Floats
        * Strings
        * Booleans
        * Objects

Collections
===========
* Lists
* Dictionaries
* Tuples


Running Python
==============
The interactive interpreter
From your shell prompt, type::

        $ python

Get something like::

        Python 2.6.1 (r261:67515, Jun 24 2010, 21:47:49) 
        [GCC 4.2.1 (Apple Inc. build 5646)] on darwin
        Type "help", "copyright", "credits" or "license" for more information.
        >>> 

The Interactive Interpreter
===========================
You can type in valid Python expressions in order to test things out::

        >>> name = "Guido von Rossum"
        >>> year = 1990
        >>> print name
        Guido von Rossum
        >>> print year
        1990
        >>> 1 + 2
        3
        >>> 

String Interpolation
====================
We assigned some variables and printed some things.

But it can be more interesting.::

        >>> print "%s made Python." % name
        Guido von Rossum made Python.

We can use *string interpolation* to substitute a variable's value into a string.

Excercise 1
===========
Make the interactive interpreter return the following string:

 "Hello, *[your name here]*"

Solution 1
==========
One way::

        print "Hello, Nolan!"

Another way::

        name = "Nolan"
        print "Hello %s" % name


Lists
=====
Lists are like arrays in Chapel.

Similar declaration, too.::

        numbers = [1, 2, 3]

However, unlike statically typed languages, lists can contain any data type.::

        my_list = ["Python", 2, 8.0, []]

Can also add to them and remove elements.

Order matters.

Tuples
======
Like lists, however, you cannot modify them once created.

Example::

        coordinates = (3, 4)

Tuple with a single element::

        weird_tuple = ("Guido",)

Parentheses are also used for grouping, hence the comma.

Iteration/Loops
===============
Used to repeat a single instruction multiple times.

Really useful for operating on collections.

For and while loops.

For Loops
=========
Structure:::

        for variable_name in collection_name:
                # do things
                
Note: everything inside the loop is *indented*!

Quick Note on Indentation
=========================
* Python uses indentation to control code structure.
* Other languages use braces ( { and } )
* Python only cares that your indentation is consistent
        * Don't mix tabs and spaces
        * Most often, people use 4 spaces as the indent-level

Back to Loops
=============
Example::

        >>>> author_names = ["Matz", "Guido", "Larry"]
        >>> for name in author_names:
        ...     print name
        ... 
        Matz
        Guido
        Larry

Exercise 2
==========
Print your name 20 times.

Hint: Instead of a list or tuple in the ``collection_name`` spot, use ``range(0,20)``.

It's kind of like Chapel's range syntax.

Solution 2
==========
One way::

        for i in range(0,20):
                print "Hello, Nolan"

Second way::
        
        name = "Nolan"
        for i in range(0,20):
               print "Hello, %s" % name

Dictionaries
============
* A collection of *key, value pairs*.
* Associates a *key* (which can be a number, string, object, whatever), with a *value*.
* Unordered - when accessing a dictionary, items may not come out in the same order they were added.


Dictionary Examples
===================
A basic dictionary::

        >>> {"shoe_size": 12}

Multiple items::

        >>> {"name": "Frank", "height": 6.0}


Accessing a Dictionary
======================
First, let's create a dictionary, with a variable::

        >>> my_dictionary = {"name": "Fred"}

Next, we can retrieve the value associated with the ``name`` key::

        >>> my_dictionary["name"]
        'Fred'

Looping with Dictionaries
=========================
Using just the dictionary in the for statement we saw before only works on the dictionary keys.

To access both, we use the ``items`` method on the dictionary. (Those will be explained soon)::

        >>>> language_authors = {"Matz": "Ruby", "Guido": "Python", 
        ... "Larry": "Perl"}
        >>> for key, value in language_authors.items():
        ...     print "%s wrote %s" % (key, value)
        ... 
        Larry wrote Perl
        Matz wrote Ruby
        Guido wrote Python

Things to note
==============
Instead of one loop variable, we had two.

When we used multiple values in string interpolation, we used a tuple.

The loop didn't print the values in the same order we put them in.

Functions
=========
Functions break up programs into logical pieces

Very much like procedures in Chapel

A stepping stone to objects.

An example::

        def adder(val1, val2):
                return val1 + val2

Functions have *names* (``adder``), take *arguments* (``val1, val2``) and can *return* a result.

Arguments
=========
We use the previous function like this::

        >>> adder(2, 3)
        5

The value ``2`` is put into ``val1``, and ``3`` into ``val2``.
``val1`` and ``val2`` are confined to the ``adder`` function::

        >>>> val1
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'val1' is not defined

This is called *scope*.

Null arguments
==============
You can also have functions without any arguments::

        def print_hello():
                print "Hello"

2 things here:
        * The parentheses are simply empty.
        * Notice we didn't return anything; in Python we don't have to.

Interlude - Using Python Files
==============================
You can use ``gedit`` to edit Python files, saving them with the extension ``.py``.

Then, you can run the files with this command::

        $ python my_file.py

Control Flow
============
Python uses ``if`` statements that look similar to Chapel's, but without the braces.

Basic structure::

        if something:
                transform(1,2)
        elif something_else:
                transform(2,3)
        else:
                transform(3,4)

Check if a value is in a collection
===================================
Using a conditional with the ``in`` keyword to see if a particular value is contained in a collection::

        >>> if "Yes" in ["Yes", "No"]:
        ...     print "Yep, it's there."
        ... 
        Yep, it's there.
        >>> if "Joe" not in ["Sam", "Frank"]:
        ...     print "Joe's not there."
        ... 
        Joe's not there.


Exercise 3
==========
Create a function that returns "weekday" if a day's name is a weekday, "weekend" if it's not.

Hints:
        * Just worry about lower case values
        * Getting user input::

                >>>> day = raw_input("Input a day's name >> ")
                Input a day's name >> Monday
                >>> day
                'Monday'

Bonus: If the word given isn't a valid calendar day, return "neither"

Solution 3
==========
.. include:: solutions/solution3.rst
               
Object Oriented Programming
===========================
* Object-oriented programming tries to model program strutures after things in the real world.
* Objects have:
        * *properties* that describe them (the bike is red)
        * *methods* that make them do things (the man runs).
* Together, these are called *members*
* Benefit: information is contained only in the area it's necessary ("information hiding")
* Objects are:
        * defined by writing a *class*
        * created by *instantiating* a class



Classes
=======
Think of classes like a *template* for objects; it describes how they will work

But, the objects contain specific information

Example
=======
* The Car Class describes cars: 
        * They have four wheels, color(s), number of seats, make, model, VIN, 
          can accelerate, deccelerate, turn, etc.
* The *actual* color, number of seats, VIN, make, model corresponds to the specific car.
* The *verbs* (the things they can do) are shared amongst all of them.

Example
=======
* The Dog Class describes dogs: They have a color, four legs, eye color, breed(s), can bark, run, etc.
* Fido is a black labrador
* Butch is a white bulldog


Making the connection
=====================
* Properties are *variables* - these can be any valid data type, including other objects!
* Methods are *functions* - these *do* things, and are common to all instances of the object
* Objects hold *state* in their properties, which is then changed by methods.

Defining a class
================
Example::

        >>>> class Dog(object):
        ...     def __init__(self, name=None, breed=None):
        ...             self.name = name
        ...             self.breed = breed
        ...     def bark(self):
        ...             print '%s says, "Woof!"' % self.name
        ...     def bark(self, target):
        ...             print "%s barks at %s!" % (self.name, target.name)
        ... 
        >>> fido = Dog(name="Fido", breed="Black Lab")
        >>> fido.bark()
        Fido says, "Woof!"

Things of note
==============
* All classes:
        * should be defined as ``class ClassName(object)``
                * ``ClassName`` inherits from ``object``.
        * define an initializer function, ``__init__``
                * This is a "magic method" that Python uses.
                * Similar to C++/Java constructors - it sets up initial state

Things of note
==============
* All methods take ``self`` as the first argument
* Different methods can have the same name, if they take different number of arguments.
* ``self`` is *not* passed in when you call the function; Python's interpreter uses it, not the programmer.
* Variables attached to ``self`` can be accessed in any other method in that class.
* I snuck in named arguments there; done for clarity.

More Theory: Inheritance
========================
* Classes can *inherit* from others.
        * This means that the *subclass* shares properties and methods with it's *superclass*
        * Also referred to as *child* and *parent* classes

Examples:

* A parent class could be Vehicle, and subclasses would be Car, Motorcycle, Truck, Tractor, etc
* Another parent class could be Animal, subclasses being Cat, Dog, Giraffe, Elephant, etc

Hierarchies
=========== 
You can also have hierarchies:

* Animal
        * Mammal
                * Dog
                * Cat
        * Bird
                * Eagle

Inheritance in Python
=====================
``class ChildClass(ParentClass)``

except for the parent class, which looks like

``class ParentClass(object)``

Why?  

* ``object`` is a type, just like ``int`` or ``str``.  Helps Python allocate memory correctly.

Exercise 4
==========
Create a Python class that represents a mathematical vector (http://en.wikipedia.org/wiki/Euclidean_vector)

Vectors are pairs of x, y coordinates.  We want the following members:

* x coordinate
* y coordinate
* adding 2 vectors (x1 added to x2, y1 added to y2)
* subtracting 2 vectors (x1 minus x2, y1 minus x2)
* a __repr__(self) method that returns the coordinates as the string "(x, y)"

Exercise 4 Hints
================
Should look something like this::

        v1 = Vector(1,3)
        v2 = Vector(8,9)
        v3 = v1.add(v2)
        print v3
        (9, 12)

Bonus: Write a method that multiplies both x and y by a single number (scalar multiplication)

Solution 4
==========
.. include:: solutions/solution4.rst


Modules and Packages
====================
* Python code is organized into modules and packages.
* *Modules* are individual Python files.
* *Packages* are directories that contain Python modules
* Modules and packages are used to distribute re-usable code.

Standard Library
================
* Python has a philosophy of "batteries included".
* LOTS of modules/packages bundled with Python.
* Examples::

        os
        zlib
        datetime
        hashlib
        threading
        socket
        unittest

* External packages, too, like SciPy, NumPy, PyCUDA, Django, SQLAlchemy, Pygments, etc

Using packages and modules
==========================
2 forms:

* ``import os``
* ``from os import path``

Getting help with packages/modules
==================================
* Use the ``dir`` function to inspect an object's members, packages and modules included
* Use the ``help`` function to get help for an object.

Example (output shortened)::

        >>>> import os
        >>> dir(os)
        [.... 'walk', 'write']
        >>> help(os.walk)
        Help on function walk in module os:

        walk(top, topdown=True, onerror=None, followlinks=False)
            Directory tree generator.



Exercise 5
==========
Using the vector class we created last time, add a ``length`` method to your vector class
that does the following:

* Squares x and y (``**`` is the exponential operator)
* Add the squares together
* Return the square root of that sum

Use the ``sqrt`` function from the ``math`` package.

Solution 5
==========
.. include:: solutions/solution5.rst
        
Python 2 or 3?
==============
For most things, Python 2 is probably the best choice.

* More mature libraries available
* Better tested

However, Python 3 is the future.

* Python 2.7 is the last release of the 2 line.
* Overall, a much better language.

Further Resources
=================

* Python Homepage: http://python.org
* Learn Python the Hard Way: http://learnpythonthehardway.org/ (2nd edition released today!)
* Learning the Zen of Python - from the Python prompt, type:::

        import this

* Also: The Pragmatic Programmer, by Andrew Hunt and David Thomas
