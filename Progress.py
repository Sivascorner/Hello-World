#!/usr/bin/env python
import signal
import sys
import time
def signal_handler(signal, frame):
 
     
   print 'You pressed Ctrl+C!'
   sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def progressbar():

 for i in range(100):

 # sys.stdout.write("\r%i" % i)
   print "\r%i{0}".format(i) %i,
   sys.stdout.flush()
   time.sleep(1)




print 'Press Ctrl+C'
print progressbar()
signal.pause()
