set terminal pngcairo size 1400,800
set output 'plot.png'

set autoscale                        
set title "Part 3"
set xlabel "Time"
set ylabel "RPS (1-minute rate)"

set xdata time
set timefmt "%H:%M:%S"

plot    "plot.tsv" using 1:2 title '500s' with lines , \
        "plot.tsv" using 1:3 title '200s' with lines , \
        "plot.tsv" using 1:4 title '404s' with lines