#! /usr/bin/python3

import sys
import random
import time
import urllib2

def generateRequest(url):
	try:
		urllib2.urlopen(urllib2.Request(url))
	except urllib2.HTTPError:
		pass

if __name__ == '__main__':
	url = str(sys.argv[1])
	desiredRPS = int(sys.argv[2])
	jitter = float(sys.argv[3])

	urlFail = url + "fail"
	urlOther = url + "other"

	actualRPS = random.randint(int(desiredRPS * (1.0 - jitter)), int(desiredRPS * (1.0 + jitter)))

	while True:
		startTime = time.time()

		i = 0
		while (i < actualRPS) and (time.time() - startTime < 1.0):
			i += 1

			urlTypeInt = random.randint(0, 10) % 7

			if urlTypeInt in [0, 2, 4, 6]:
				generateRequest(url)
			elif urlTypeInt == 3:
				generateRequest(urlFail)
			else:
				generateRequest(urlOther)