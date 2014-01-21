import os
from gps import *
from time import *
import time
import threading

#Global variable is usually none. so better leave it empty.
gpsd = None 

os.system('clear') 
class GpsPoller(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		global gpsd #bring it in scope
		gpsd = gps(mode=WATCH_ENABLE) 
		self.current_value = None
		self.running = True 

	def run(self):
		global gpsd
	while gpsp.running:
			gpsd.next() 

if __name__ == '__main__':
	gpsp = GpsPoller() 
	try:
		gpsp.start() 
		while True:
		
			os.system('clear')

	
		print ' GPS reading'
		print '---------'
		print 'latitude    ' , gpsd.fix.latitude
		print 'longitude   ' , gpsd.fix.longitude
		print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
		print 'altitude (m)' , gpsd.fix.altitude
		print 'ept         ' , gpsd.fix.ept
		print 'speed (m/s) ' , gpsd.fix.speed
		print 'climb       ' , gpsd.fix.climb
		print
		print 'sats        ' , gpsd.satellites
	
	  time.sleep(5) #set to whatever
	
	except (KeyboardInterrupt, SystemExit): 
		print "\nKilling Thread..."
		gpsp.running = False
		gpsp.join() 
