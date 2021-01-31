list1=[1,2,2,3,4,5,7]
list2=[]
list3=[]
list4=[]
list5=[]
for i in list1:
    list2.append(i)

print "This is list1"
print list1[0:]
print "This is list2"
print list2[0:]

list3 = [i for i in list1]
print "This is list3 using list comprehension"
print list3

#if we want squares of each n in list1 into list4 using list comprehension

list4 = [i*i for i in list1]
print "These are squres :)"
print list4

#lambda is an anonymous function and we can use it with map to get squares in a list
list5 = list(map(lambda x:x*x,list1))
print list5

