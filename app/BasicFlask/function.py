Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def printList()
SyntaxError: invalid syntax
>>> def printlist()
SyntaxError: invalid syntax
>>> def printList():
	num_list=range(3)
	return num_list

>>> printList()
range(0, 3)
>>> def printList(upper_limit):
	num)list = range(upper_limit)
	
SyntaxError: invalid syntax
>>> def printList(upper_limit):
	num_list = range(upper_limit)
	print('list: %s' % num_list)

	
>>> printList(5)
list: range(0, 5)
>>> printList(2)
list: range(0, 2)
>>> 
