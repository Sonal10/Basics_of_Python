def sq_nums(nums):
    for i in nums:
        yield (i*i)

my_nums = sq_nums([1,2,3,4,5])

for num in my_nums:
    print num

# how to do this with list comprehension

def sq_nums_list_comprehension(numbr):
    my_gen = []
    my_sq_list = (i*i for i in numbr)
    for i in my_sq_list:
       print i
    # We can also map the genrator to a list
        #print list(my_sq_list)
    

sq_nums_list_comprehension([1,2,3,4,5,6])





