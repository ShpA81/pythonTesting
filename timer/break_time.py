import time
import webbrowser

total_breaks = 3
break_count = 0

print("this program started on " + time.ctime())
while (break_count < total_breaks):
    time.sleep(2)
    webbrowser.open("http://www.mindful-trinity.com")
    break_count = break_count + 1

print "finished"
