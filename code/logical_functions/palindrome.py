string1 = raw_input("Please enter a string for checking for palindrome : ")
#rev_str = reversed(string1)

list1 = []
list2 = []

for i in string1:
    list1.append(i)
    
#print list1[:]

print "This is list 2 after reversal" 
list2 = list1[::-1]
#print list2[:]

if list1 == list2: #To be noted. This comparision takes into account the order of the elements in the list.
    print "Its a palindrome"
else:
    print "Sorry, not a palindrome"
