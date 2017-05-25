#FizzBuzz

while 1:
    
    
    try:
        i=int(raw_input("Please enter a number or press 0001 to exit"))
        if i == 0001:
            raise Exception
        if i % 5== 0 and i % 3 == 0:
            print ("FizzBuzz")
        elif i%3==0:
            print ("Fizz")
        elif i%5==0:
            print ("Buzz")
        else:
            print ("Sorry, it ain't divisible by 3 or 5")

    except ValueError as v:
            print "Invalid Input, please try again"
    except Exception as e:
        break

