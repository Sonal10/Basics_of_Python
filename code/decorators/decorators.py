#Function Decorator

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print "This executes before {}".format(original_function.__name__)
        return original_function(*args, **kwargs)
        
    return wrapper_function


@decorator_function
def display(name,value):
    print "Hi {} with value {}".format(name,value)

display("Sonal",1)

#Decorator executes a function that we pass in. What happens behind the scenes:
# decorator_display = decorator_function(display)
# decorator_display()
#Steps that happen :
#1. Decorator_function gets called with the display function as an argument.
#2. This executes wrapper function which then finally returns the wrapper function.
#3.This is store in decorated_display waiting to be executed and is executed in the second cline.
#4. This leads to execution of original function.

#Class as a decorator

class decorator_class(object):
    def __init__(self,original_function):
        self.original_function = original_function

    def __call__(self,*args,**kwargs):
        print "Call method : This executes before {}".format(self.original_function.__name__)
        return self.original_function(*args, **kwargs)



@decorator_class
def display_info(name,value):
    print "Hi {} with value {}".format(name,value)

display_info("Swati",2)




