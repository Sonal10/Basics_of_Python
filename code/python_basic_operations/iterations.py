list1=[1,2,3,4]
for i in list1:
    print i

my_tup=(1,2,3,4)
for i in my_tup:
    print i

my_dict={"one":1,"two":2,"three":3}
for key,value in my_dict.iteritems():
    print "My key is {} and my value is {}".format(key,value)

my_set={1,2,3,4}
#set is a list with nu duplicates

for i in my_set:
    print i
