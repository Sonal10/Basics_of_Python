def add(n1,n2):
    return n1+n2

def mult(n1,n2):
    return n1*n2

def sub(n1,n2):
    return n1-n2

def divide(n1,n2):
    return n1/n2

def exp(n1,n2):
    return n1**n2

def mod(n1,n2):
    return n1%n2

opers = { '+' : add,
          '-' : sub,
          '*' : mult,
          '/' : divide,
          '^' : exp,
          '%' : mod}

while True:
    n1= raw_input("Please enter what would you like to do: 1. + 2. - 3. * 4. \ 5. ^ 6. % >")
    if n1:
        try:    
            n2=int(raw_input("Please enter two numbers for the above mentioned operation. Note: Press enter after entering the first number and then press the second"))
            n3=int(raw_input())
            print (opers[n1](n2,n3))

        except Exception:
            print "Sorry invalid input, please try again."
    else:
        break
        
    


