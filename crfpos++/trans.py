#!/usr/bin/env python
# coding=utf-8

with open("people-daily.txt") as f:
    e = open("output.txt","w")
    readlines = f.readlines()
    for i in readlines:
        strip = i.strip()
        split = strip.split(" ")
        for c in split:
            d = c.split("/")
            print d
            if d ==['']:
                continue
            if d[0].startswith('19980'):
                continue
            e.write(d[0] +"\t" + d[1] + "\n")
        e.write("\n")
    e.close()
