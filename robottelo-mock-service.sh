#!/usr/bin/sh

# a mock script that writes a "version" value to a file and then runs in an infinite loop

echo "$(rpm -q robottelo-mock-service --queryformat='%{version}')" > /var/log/robottelo-mock-service/service.log
while true
do
 sleep 3600
done
