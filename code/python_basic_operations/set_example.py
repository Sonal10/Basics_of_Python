"""
 Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python
 """

import random as r

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print list(set(a) & set(b)) #In one line of python

#Random generation of two lists

list1 = [r.randrange(1,10) for i in range(10)]
print "First random list :" + str(list1)

list2 = [r.randrange(1,15) for i in range(15)]
print "Second random list" + str(list2)

print list(set(list1) & set(list2))




