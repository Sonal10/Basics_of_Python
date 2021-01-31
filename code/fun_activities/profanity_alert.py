#This method read_text() shows how to raed from files
def read_text():

   quotes = open("C:\Users\Sonal Somani\Desktop\Personal\upstur_derrick.txt")
   contents_of_file = quotes.read()
   print(contents_of_file)
   length = len(contents_of_file[0:10])
   print(length)
   quotes.close()

#Profanity checker from a file with list of words
def profanity_check(text_to_check):
   
   text_file = open("C:\Python27\Profanity.csv","r")
   words = text_file.read().split('\n')
   print words
   #print(lines)
   #for i in lines:
    #  print i
     # if word == i:
      #   prof=1
      #else:
       #  prof=0
   prof =0
   for word in words:
      
      if text_to_check == word:
         
         prof+=1
         print word
      
               

   if prof > 0:
         print "Its a profane word."
   else:
         print "We have no knowledge of this word."
         
   
while True:
      check = raw_input("Please enter the word you wish to check for profanity: ")
      if check:
         try:
            profanity_check(check)

         except ValueError as e:
            print "Invalid Input"

      else:
         break
               
      
      
      
   

