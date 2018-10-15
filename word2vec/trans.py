#!/usr/bin/env python
# coding=utf-8

def trans(filename, out_file):
    with open(filename) as f:
        with open(out_file, "w") as o:
            lines = f.readlines()
            for line in lines:
                words = line.strip().split()
                word = [w.split("/")[0] for w in words]
                o.write("".join(word) + "\n")

if __name__ == '__main__':
    trans("msr_train.txt", "init.txt")
