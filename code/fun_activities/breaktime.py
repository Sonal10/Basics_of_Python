import webbrowser
import time

total_breaks=6
break_count=0

print("This program started on"+time.ctime())
while(total_breaks<break_count):
    time.sleep(7200)
    webbrowser.open("https://www.youtube.com/watch?v=JGwWNGJdvx8",new=2,autoraise=True)
    break_count=break_count+1

    
