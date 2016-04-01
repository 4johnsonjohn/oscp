#!/bin/bash
#Domain
  rm index.html
  wget --no-check-certificate $1
  echo $1
  grep -o '[A-Za-z0-9_\.-]*\.*'$1 ./index.html | sort -u
  grep -o '[A-Za-z0-9_\.-]*\.*'$1 ./index.html | sort -u > url.txt
  for url in $(cat url.txt);do
	host $url | grep "has address" | cut -d " " -f4
  done

