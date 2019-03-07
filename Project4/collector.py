#! /usr/bin/python3

import sys
import time
import urllib2

if __name__ == '__main__':
	urlStats = str(sys.argv[1]) + "stats"
	interval = float(sys.argv[2])

	with open("collectorOutput.tsv", "a") as outStream:
		while True:
			responseArray = urllib2.urlopen(urllib2.Request(urlStats)).read().splitlines()
		
			for i in range(0, len(responseArray)):
				responseArray[i] = str(responseArray[i]).rpartition(': ')[2]

			outStream.write(responseArray[0] + "\t" + responseArray[1] + "\t" + responseArray[2] + "\t" + responseArray[3] + "\n")

			time.sleep(interval)
	outStream.close()