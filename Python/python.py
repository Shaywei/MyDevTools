# With Statement
'''
"with" statement trying to solve code repetition of this sort:

    set things up
    try:
        do something
    finally:
        tear things down

and have the "tear things down" reusable
'''

class controlled_execution(object):
    def __enter__(self):
        pass
        #set things up
        #return thing
    def __exit__(self, type, value, traceback):
        pass
        #tear things down

# Descriptors

'''
http://stackoverflow.com/questions/5738470/whats-an-example-use-case-for-a-python-classmethod

In general, a descriptor is an object attribute with binding behavior, one whose attribute access has been overridden by methods in the descriptor protocol. Those methods are __get__(), __set__(), and __delete__(). If any of those methods are defined for an object, it is said to be a descriptor.he default behavior for attribute access is to get, set, or delete the attribute from an objects dictionary. For instance, a.x has a lookup chain starting with a.__dict__['x'], then type(a).__dict__['x'], and continuing through the base classes of type(a) excluding metaclasses.

Descriptors are a powerful, general purpose protocol. They are the mechanism behind properties, methods, static methods, class methods, and super(). They are used throughout Python itself to implement the new style classes introduced in version 2.2. 

Descriptor protocol

    descr.__get__(self, obj, type=None) --> value

    descr.__set__(self, obj, value) --> None

    descr.__delete__(self, obj) --> None

__get__ is invoked whenever we use the '.' operator (obj.d)
__set__ is invoked whenever we use the '.' with assignment (obj.d = new_value)

* If both __get__ and __set__ are implemented, the descriptor is called data descriptor

* If only __get__ is implemented, it is called non-data descriptor.

The important points to remember are:

    * descriptors are invoked by the __getattribute__() method

    * overriding __getattribute__() prevents automatic descriptor calls    __getattribute__() is only available with new style classes and objects

    * object.__getattribute__() and type.__getattribute__() make different calls to __get__().

    * data descriptors always override instance dictionaries.

    * non-data descriptors may be overridden by instance dictionaries.

Descriptor are used to implement decorators such as classmethod, staticmethod, properties..
'''

Example for properties:

class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
'''
Common uses for properties:
    * Not to declare a setter method if you want to make something read-only
    * Do a validation on setter method and raise exception if needed
    * Implement lazy-evalutaion by delaying heavy calculation to when a property is read.
'''

# Method, @classmethod, @staticmethod
'''
http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
'''

class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x    

a=A()
a.foo(1)
a.class_foo(1)
A.class_foo(1)

'''
A common use for class methods is to create inheritable alternative constructors.
A known example is: dict.formkeys()
'''


# A great explanation about metaclasses
'''
http://stackoverflow.com/a/6581949
'''