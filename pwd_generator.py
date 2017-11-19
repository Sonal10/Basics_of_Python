"""
Write a password generator in Python.
Be creative with how you generate passwords -
strong passwords have a mix of lowercase letters,
uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time
the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords,
pick a word or two from a list.
"""
import random as r

def pwd_gen(strength):
    a=[]
    if strength == "Weak":
        a = open("C:\Python27\words.csv",'r').read().split('\n')
        #print a
        b = [i for i in a if len(i) > 8]
        pwd1 = r.choice(b)
        
        #if len(pwd1) < 8:
            #pwd2 = r.choice(a)
            #pwd1 = pwd2 + pwd1
        print "Your new password is " + pwd1
        
    elif strength == "Medium":
        a = open("C:\Python27\words.csv",'r').read().split('\n')
        #print a
        pwd1 = r.choice(a)
        if len(pwd1) < 7:
            pwd2 = r.choice(a)
            pwd1 = pwd2 + pwd1
        pwd1 = pwd1 + str(r.randrange(1,100))
        #pwd1 = pwd1 + str(r.choice(['!','#','@','$','%','^','&','*','-','_','~']))
        print "Your new password is " + pwd1
    elif strength == "Strong":
        a = open("C:\Python27\words.csv",'r').read().split('\n')
        #print a
        pwd1 = r.choice(a)
        #print pwd1
        if len(pwd1) < 7:
            pwd2 = r.choice(a)
            pwd1 = pwd2 + pwd1
            #print pwd1
        pwd3 = pwd1[0:2].upper()
        pwd1 = pwd3 + pwd1[2:]
        #print pwd1
        pwd1 = pwd1 + str(r.randrange(1,100))
        pwd1 = pwd1 + str(r.choice(['!','#','@','$','%','^','&','*','-','_','~']))
        print "Your new password is " + pwd1


strength_of_pwd = str(raw_input("Please tell the strength of the pwd that you would prefer? \
\ 1. Weak 2. Medium 3. Strong"))
pwd_gen(strength_of_pwd)



