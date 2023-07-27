File tests the MyList Class
===========================

Usage:
	>>> MyList = _import_('1-my_list').MyList
	>>> my_list = MyList()
	>>> my_list.append(1)
	>>> my_list.append(5)
	>>> my_list.append(2)
	>>> my_list.append(6)
	>>> my_list.append(5)
	>>> my_list.print_sorted()
	[1, 2, 5, 5, 6]

Tests Case: Print an empty list
---------------------------------

::
	>>> my_list.clear()
	>>> my_list.print_sorted()
	[]

::

Test Case: A list with only one element
---------------------------------------

::
	>>> my_list.append(2)
	>>> my_list.print_sorted()
	[2]

::

Test Case: A list with negative integers
-----------------------------------------

::
	>>> my_list.append(-2)
	>>> my_list.append(-7)
	>>> my_list.append(0)
	>>> print(my_list)
	[2, -2, -7, 0]
	>>> my_list.print_sorted()
	[-7, -2, 0, 2]

::

Test Case: 1 positional argument
--------------------------------

::
	>>> my_list.print_sorted(1)
	Traceback (most recent call last):
	TypeError: print_sorted() takes 1 positional argument but 2 were given

::

Test Case: Checking for documentation
--------------------------------------

::
	>>> docs = _import('1-my_list').doc_
	>>> len(docs) > 1
	True
	>>> docs = _import('1-my_list').MyList.doc_
        >>> len(docs) > 1
        True
