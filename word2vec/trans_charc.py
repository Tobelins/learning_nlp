#!/usr/bin/env python
# coding=utf-8

with open("init.txt") as d:
    with open("try.txt","w") as f:
        readlines = d.readlines()
        for readline in readlines:
            readline = readline.strip().decode("utf-8")
            word = len(readline)
            for i in range(0, word):
                f.write(readline[i].encode("utf-8")+" ")
            f.write("\n")        
            

            
