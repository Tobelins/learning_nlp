#!/usr/bin/env python
# coding=utf-8
with open("test.rst") as f:
    lines = f.readlines()
    correct = 0
    total = 0
    for line in lines:
        line = line.strip()
        tags = line.split("\t")
        if tags ==['']:
            continue
        if tags[1] == tags[2]:
            correct = correct + 1
        total = total + 1
    print(correct/float(total))

        
