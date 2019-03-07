#!/bin/bash

# generate input txt file
find * -type f | grep \.ogg | cut -d / -f 1,2,3,4,5,6 | sort -u
