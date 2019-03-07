#! /usr/bin/env/ python3

import sys
from collections import defaultdict
import re

def buildDictSegCook(fileName):
	dictSegCook = defaultdict(list)

	with open(fileName) as fileStream:
		for line in fileStream:
			cookie = re.findall(':\s([A-Fa-f0-9]+)\s', line)
			segments = re.findall('.[0-9]+_[0-9]+', line)

            		if cookie and segments:
				for segment in segments:
					dictSegCook[segment].append(cookie[0])

	fileStream.close()

	return dictSegCook

def buildDictCookSeg(inputDict):
	dictCookSeg = defaultdict(list)

	for segment, cookies in inputDict.items():
		for cookie in cookies:
			dictCookSeg[cookie].append(segment)

	return dictCookSeg

def findExtraElements(baseDict, testDict):
    	extraElementsDict = defaultdict(list)

    	for key in testDict.keys():
        	if not key in baseDict.keys():
			if testDict[key]:
            			extraElementsDict[key] = testDict[key]
        	else:
			extraElementsSet = set(testDict[key]) - set(baseDict[key])

			if extraElementsSet:
				extraElementsDict[key] = list(extraElementsSet)

    	return extraElementsDict

def findMissingElements(baseDict, testDict):
    	missingElementsDict = defaultdict(list)

    	for key in baseDict.keys():
        	if key in testDict.keys():
			missingElementsSet = set(baseDict[key]) - set(testDict[key])

			if missingElementsSet:
				missingElementsDict[key] = list(missingElementsSet)
        	else:
			if baseDict[key]:
				missingElementsDict[key] = baseDict[key]

    	return missingElementsDict

def printDict(inputDict):
    	lineCount = 0

    	for key in sorted(inputDict.keys()):
        	print str(lineCount),
		print "\t",
		print key,
		print "\t",
		print str(len(inputDict[key])),
		print "\t",
		print sorted(inputDict[key])

        	lineCount += 1

	print

def main(args):
	baseDictSegCook = buildDictSegCook(sys.argv[1])
	testDictSegCook = buildDictSegCook(sys.argv[2])

	baseDictCookSeg = buildDictCookSeg(baseDictSegCook)
	testDictCookSeg = buildDictCookSeg(testDictSegCook)

	segmentsGainedExtraCookies = findExtraElements(baseDictSegCook , testDictSegCook)
    	print "Segments that gained extra cookies:",
	print str(len(segmentsGainedExtraCookies)),
	print "/",
	print str(len(baseDictSegCook))

    	printDict(segmentsGainedExtraCookies)

	segmentsLostCookies = findMissingElements(baseDictSegCook , testDictSegCook)
    	print "Segments that lost cookies:",
	print str(len(segmentsLostCookies)),
	print "/",
	print str(len(baseDictSegCook))

    	printDict(segmentsLostCookies)

	cookiesAssignedExtraSegments = findExtraElements(baseDictCookSeg, testDictCookSeg)
    	print "Cookies assigned to extra segments:",
	print str(len(cookiesAssignedExtraSegments)),
	print "/",
	print str(len(baseDictCookSeg))

   	printDict(cookiesAssignedExtraSegments)

	cookiesOmittedFromSegments = findMissingElements(baseDictCookSeg, testDictCookSeg)
    	print "Cookies omitted from segments:",
	print str(len(cookiesOmittedFromSegments)),
	print "/",
	print str(len(baseDictCookSeg))

    	printDict(cookiesOmittedFromSegments)

if __name__ == '__main__':
    main(sys.argv)