
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
A object-oriented, dynamically typed, interpreted, general purpose programming language
Open source, BSD-like license
Supported on lots of platforms

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
Languages like Chapel, C, Java require variables to have their type declared on creation
Python does not; a variable can hold any kind of value.

Examples::

	a = "a string"
	a = 1

Dynamically Typed
=================
Variable's *properties* are important, not it's data type.

Also known as "duck typing".
	* "If it walks like a duck and quacks like a duck, it's a duck".

Object-Oriented
===============
Data and the functions related to it is associated through objects
Objects are instances classes.
More on this later.


Data Types
==========
Several generic, basic data types:
        * Integers
        * Floats
        * Strings
        * Booleans
        * Objects


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
You can type in valid Python expressions in order to test things out.::
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


Lists
=====
Lists are like arrays in Chapel.


Python 2 or 3?
==============
For most things, Python 2 is probably the best choice.
        * More mature libraries available
        * Better tested
However, Python 3 is the future.
        * Python 2.7 is the last release of the 2 line.
        * Overall, a much better language.
