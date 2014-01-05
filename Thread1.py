import threading
import time
class count_stuff(threading.Thread):
    """
        A thread class that will count a number, sleep and output that number
    """
   
    def __init__ (self, start_num, end):
        self.num = start_num
        self.end = end
        threading.Thread.__init__ (self)
   
    def run(self):
        while True:
            if self.num != self.end:
                self.num += 1
                print "Outputting: ", str(self.num)
                time.sleep(5)
            else:
                break
       
myThread1 = count_stuff(6,10)       
myThread = count_stuff(1, 5)
myThread.start()
myThread1.start()
