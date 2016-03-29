#!/bin/bash
#scan a specific host ie megacorpone.com for available services aka ftp . www. mail etc. The list containing this is called commonurl.tx
for name in $(cat commonurl.txt);do
	host $name.$1|grep "has address" | cut -d " " -f1,4
done
