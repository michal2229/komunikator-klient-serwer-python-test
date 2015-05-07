import msvcrt
import time


while 1:
    x = msvcrt.kbhit()
    if x: 
        print msvcrt.getch()
    else:
        print "z"
    
    time.sleep(1) # delays for 5 seconds
