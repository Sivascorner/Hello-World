import os
import threading

import time
duration = 2
count = 0

#os.system("ls -lart")
class stat(threading.Thread):
    """
        A thread class that will count a number, sleep and output that number
    """
   
    def __init__ (self, func_name,duration):
        self.func_name = func_name
        self.duration = duration
        print "Inside stat"
        
        threading.Thread.__init__ (self)
   
    def run(self):
        while True:
            
#             if self.func_name:
            if self.func_name == "mem_stats":
             self.test=mem_stats()
             print self.test   
             time.sleep(self.duration)
            elif self.func_name == "cpuinfo":
              self.test = cpu_info()
              print self.test
              time.sleep(self.duration)              

def mem_stats():
    with open('/proc/meminfo') as f:
        for line in f:
            if line.startswith('MemTotal:'):
                mem_total = int(line.split()[1]) * 1024
            elif line.startswith('Active: '):
                mem_active = int(line.split()[1]) * 1024
            elif line.startswith('MemFree:'):
                mem_free = (int(line.split()[1]) * 1024)
            elif line.startswith('Cached:'):
                mem_cached = (int(line.split()[1]) * 1024)
            elif line.startswith('SwapTotal: '):
                swap_total = (int(line.split()[1]) * 1024)
            elif line.startswith('SwapFree: '):
                swap_free = (int(line.split()[1]) * 1024)
    return (mem_active, mem_total, mem_cached, mem_free, swap_total, swap_free)

def cpu_times():

    
    with open('/proc/stat') as f:
        line = f.readline()
    
    cpu_times = [int(x) for x in line.split()[1:]]
    
    return cpu_times




def __cpu_time_deltas(sample_duration=1):
    """Return a sequence of cpu time deltas for a sample period.
elapsed cpu time samples taken at 'sample_time (seconds)' apart.
each value in the sequence is the amount of time, measured in units
of USER_HZ (1/100ths of a second on most architectures), that the system
spent in each cpu mode: (user, nice, system, idle, iowait, irq, softirq, [steal], [guest]).
on SMP systems, these are aggregates of all processors/cores.
"""
    
    with open('/proc/stat') as f1:
        with open('/proc/stat') as f2:
            line1 = f1.readline()
            time.sleep(sample_duration)
            line2 = f2.readline()
    
    deltas = [int(b) - int(a) for a, b in zip(line1.split()[1:], line2.split()[1:])]
    
    return deltas

def cpu_percents(sample_duration=duration):
    
    
    deltas = __cpu_time_deltas(sample_duration)
    print deltas
    total = sum(deltas)
    percents = [100 - (100 * (float(total - x) / total)) for x in deltas]

    return {
        'user': percents[0],
        'nice': percents[1],
        'system': percents[2],
        'idle': percents[3],
        'iowait': percents[4],
        'irq': percents[5],
        'softirq': percents[6],
    }
count =0    
def cpu_info():
  
   while True: 
    with open('/proc/cpuinfo') as f:
        cpuinfo = {'processor_count': 0}
        for line in f:
            if ':' in line:
                fields = line.replace('\t', '').strip().split(': ')
                # count processores and filter out core specific items
                if fields[0] == 'processor':
                    cpuinfo['processor_count'] += 1
                elif fields[0] != 'core id':
                    try:
                        cpuinfo[fields[0]] = fields[1]
                    except IndexError:
                        pass
        #count=count+1    
#         print memstat.name,cpuinfo      
        return cpuinfo

    
#print mem_stats()
#print cpu_percents()
#print cpu_info()
#
#while True:
# memstat = threading.Thread(name='memstats', target=mem_stats)
# memstat.setDaemon(True)
# print "\n"
# cpuinfo = threading.Thread(name='cpuinfo', target=cpu_info)
# 
# cpupercent = threading.Thread(name='cpupercent',target=cpu_percents,args=(duration,)) # use default name
# 
# memstat.start()
# cpuinfo.start()
# cpupercent.start()
myThread1 = stat("mem_stats",1)       
myThread = stat("cpuinfo", 1)
myThread.start()
myThread1.start()
