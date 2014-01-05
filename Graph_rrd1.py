import sys
import time
import random
import rrdtool
 
total_input_traffic = 0
total_output_traffic = 0
 
while 1:
 total_input_traffic += random.randrange(1000, 1500)
 total_output_traffic += random.randrange(1000, 3000)
 ret = rrdtool.update('net.rrd','N:' + `total_input_traffic` + ':' + `total_output_traffic`)
 if ret:
  print rrdtool.error()
  time.sleep(5) 
ret = rrdtool.graph( "net.png", "--start", "-1d", "--vertical-label=Bytes/s",
 "DEF:inoctets=net.rrd:input:AVERAGE",
 "DEF:outoctets=net.rrd:output:AVERAGE",
 "AREA:inoctets#00FF00:In traffic",
 "LINE1:outoctets#0000FF:Out traffic\\r",
 "CDEF:inbits=inoctets,8,*",
 "CDEF:outbits=outoctets,8,*",
 "COMMENT:\\n",
 "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",
 "COMMENT:  ",
 "GPRINT:inbits:MAX:Max In traffic\: %6.2lf %Sbps\\r",
 "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",
 "COMMENT: ",
 "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps\\r")
  