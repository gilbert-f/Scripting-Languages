#! /usr/bin/python3

from os import system, remove

if __name__ == '__main__':
	system('gnuplot plot.p')
	remove('plot.tsv')
