

def fib_series():
    list1=[]
    a=0
    b=1
    
    list1.append(a)
    
    
    for i in range(2,20):
        a,b=b,a+b
        list1.append(a)
        
        
        

    print list1[0:]


fib_series()
    
    
