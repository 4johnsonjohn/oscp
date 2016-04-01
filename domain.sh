#!/bin/bash
rm index.html
wget $1
for url in $(grep -o 'A-Za-z0-9_\.-*\.*'/$1 index.html | sort -u); do host $url | grep "has address"|cut -d " " -f4;done
