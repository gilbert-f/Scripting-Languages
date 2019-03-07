#! /usr/bin/python3

from datetime import datetime

if __name__ == '__main__':
	with open("collectorOutput.tsv", "r") as inputStream:
		prevLineArray = (inputStream.next()).split('\t')

		for currentLine in inputStream:
			currentLineArray = currentLine.split('\t')

			if int(currentLineArray[0]) - int(prevLineArray[0]) >= 60:
				time = datetime.utcfromtimestamp(int(currentLineArray[0])).strftime('%H:%M:%S')

				RPS = [0, 0, 0]
				for i in range(0, 3):
					RPS[i] = (int(currentLineArray[i+1])-int(prevLineArray[i+1]))/60

				print str(time) + "\t" + str(RPS[0]) + "\t" + str(RPS[1]) + "\t" + str(RPS[2])

				prevLineArray = currentLineArray		
	inputStream.close()