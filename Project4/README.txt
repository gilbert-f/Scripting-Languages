Preliminaries

timeserver folder contains all the source code files to generate a localhost website and its stats page.

Part 1:
trafficgen.py is the source code for part 1.

Part 2:
collector.py is the source code for part 2.
collectorOutput.tsv is the expected output for part 2.

Part 3:
tempPlot.py is the source code to generate a temporary tsv file in 1-minute rate of the 3 time-series.
plot.py is the source code to generate the graph and clean temporary files.
plot.p is the gnuplot source code to generate the graph.
plot.png is the actual graph.

Instructions
1. Unzip HW4 zip file.
2. Use cd command on your terminal to go to HW4 directory.
3. Run "python ./timeserver/timeserver.py" to generate a localhost website.
4. Run "python ./trafficgen.py http://localhost:<PORT>/ <RPS> <jitter>" to generate traffic. The url must be in "http://localhost:<PORT>/" format.
5. Run "python ./collector.py http://localhost:<PORT>/ <interval>" to collect stats page data. The url must be in "http://localhost:<PORT>/" format.
6. Run "python ./tempPlot.py > plot.tsv" to create temporary tsv file.
7. Run "python ./plot.py" to plot the graph.