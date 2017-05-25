from functools import wraps

#Logging using decorator

def my_logger(orig_func):
    import logging
    
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level=logging.INFO)
    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        logging.info(
            'Ran with args: {}, and kwrags: {}'.format(args,kwargs))
        return orig_func(*args,**kwargs)
    return wrapper


@my_logger
def display(name,value):
    print "Hello. Welcome to my world"

display("Sonal",2)


#Timer using decorator

def my_timer(orig_function):
    import time as t
    @wraps(orig_function)
    def wrapper1(*args,**kwargs):
        t1 = t.time()
        print "Timer started"
        result = orig_function(*args,**kwargs)
        t2 = t.time()
        time_spent = t2-t1
        print "Time taken: {} ".format(time_spent)
        return result
        
    return wrapper1

@my_logger
@my_timer
#This stacking is similar to saying : timer = my_logger(my_timer(timing))
# timer()
#my_timer gets executed first and then my_logger

def timing(name, value):
    print "Do something here."
    print "Timer ends"
    


timing("Tommy",25)





