# UVa Online Judge Functional Python Solutions

The UVa Online Judge is is an online automated judge for programming problems hosted by University of Valladolid. It was created by mathematician Miguel Ángel Revilla teaching algorithms. This repository is dedicated to solving OJ problemsets using Python within the "functional" paradigmn.

## What does Functional Programming in Python Mean?

    1. Functions are to be used independent of Classes or Types and are encouraged to be used as first class values.
    2. Data modeling should be done with generic data structures: lists, sets, dictionaries, tuples instead of Classes.
    3. Operations such as iteration are replaced with higher level abstractions such as map, filter and reduce (and with generator functions used when such abstractions are not available).

Because most Python built-in types are mutable, data modeling need not be resrictred to immutable types (numbers, booleans, strings, tuples, frozensets). Funtional Python is definitely "immpure" when used as a functional language, but, unlike Java, it is also not a pure OOP lanuage, and offers many oppertunities to simulate various features of functional languages (but usually with the compromises one would expect from the language). The following offer possible ways to expand the functional toolkit but are avoided in favor of writing my own abstractions.

* [toolz](https://github.com/pytoolz/toolz/) that provides a number of typical functional programming abstractions; and
* [pyrsistent](https://github.com/tobgu/pyrsistent) provides a library of immutable data structures for use in Python.
