#!/usr/bin/env python
# coding=utf-8
import jieba
with open("init.txt") as d:
    with open("popseg.txt",'w') as f:
        readlines = d.readlines()
        for readline in readlines:
            readline = readline.strip()
            g = jieba.cut(readline)
            for j in g:
                f.write(j.encode("utf-8") + " ")
            f.write("\n")



