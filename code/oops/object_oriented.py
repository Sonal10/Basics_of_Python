import datetime


class Employee:

#class variables are available only via through class or an instance of an class but is available throughout the class
    raise_amount=1.04
    num_of_empls = 0
#instance variable : self,first, last,pay etc, they can be unique for each instance of a class

    def __init__(self ,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_empls += 1

    #regular method
    def fullname(self):
        print (self.first + " " + self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #Employee.raise_amount or self.raise_amount is essential to mention


    #class method can be created by using a class method decorator, cls is a class vraible name
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount

    # class method takes cls variable as first argument
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    #this method can be thought of as an alternative constructor


    #static methods don't pass anything automatically, they don't pass instance (self) or class (cls)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True
        

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self,first,last,pay,prog_lang):
        #super().__init__(first,last,pay)
        #Can also be done like this:
        Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang



emp_1 = Employee('Sonal','Somani',50000)
emp_2 = Employee('Swati','Sharma',0)

print(emp_1.email)
print(emp_2.email)

emp_1.fullname()
emp_2.fullname()

#In the backround this is what happens: class.method(instance_name)
Employee.fullname(emp_1)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
emp_1.raise_amount=1.05

print emp_1.raise_amount
print emp_2.raise_amount
print Employee.raise_amount
print Employee.num_of_empls

#Class variable can be overwirtten when called via class for both the class as well as the instances
# but if overwritten only via one instance, the class variable changes just for that instance
#using self.raise_amount gives us the ability to change this amount just for a single instance as well

Employee.set_raise_amount(1.06)
print emp_1.raise_amount
print emp_2.raise_amount
print Employee.raise_amount

#check emp_1.__dict__ to see why emp_1.raise_amount didn't change

emp1 = Employee.from_string("John-Doe-9000")
print emp1.pay

my_date = datetime.date(2016,7,11)
print(Employee.is_workday(my_date))

dev_1 = Employee('Sonali','Somani',50000)
dev_2 = Developer('Shreya','Sharma',6000,'python')
print dev_2.first
print dev_2.pay
dev_2.apply_raise()
print dev_2.pay
print dev_2.prog_lang

print dev_1.first
print dev_1.pay
dev_1.apply_raise()
print dev_1.pay

#isinstance(dev_1,Developer)
#issubclass(Developer,Employee)
