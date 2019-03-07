#!/bin/bash

# Problem 1
echo -n 'Total Tracks: '
find Music -type f | wc -l

# Problem 2
echo -e -n '\nTotal Artists: '
ls -ld Music/*/* | cut -d / -f 3 | sort | uniq | wc -l

# Problem 3
echo -e '\nMulti-Genre Artists:'
ls -1d Music/*/*/ | cut -d / -f 3 | sort | uniq -d

# Problem 4
echo -e '\nMulti-Disk Albums:'
ls -1d Music/*/*/*/disk1 | cut -d / -f 4 | sort | uniq
