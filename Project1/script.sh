#!/bin/bash

# Problem 1
echo -n 'Total Tracks:'
find Music -name *.ogg | wc -l

echo ''

# Problem 2
echo -n 'Total Artists:'
find Music -mindepth 2 -maxdepth 2 -type d | cut -d / -f 3 | sort | uniq | wc -l

echo ''

# Problem 3
echo 'Multi-Genre Artists:'
find Music -mindepth 2 -maxdepth 2 -type d | cut -d / -f 3 | sort | uniq -d

echo ''

# Problem 4
echo 'Multi-Disk Albums:'
find Music -mindepth 4 -maxdepth 4 -type d | cut -d / -f 4 | sort | uniq
