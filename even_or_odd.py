import functools
numbers = [1,2,3,4,5,6,7,8,9,10]

def evens(num):
        if num % 2 == 0:
            return True
        else:
            return False

even_list = list(filter(evens,numbers))
print even_list

#print sum using functools

#sum = functools.reduce(sum,numbers)
#print sum
