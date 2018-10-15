#!/usr/bin/env pythonmZ# coding=utf-8
with open("pre_word_vec_10.txt") as e:
    with open("try.txt")as f:
        with open("output.txt","w") as g:
            dict = {}
            readlines = e.readlines()
            for readline in readlines:
                readline = readline.strip()
                word = readline.split(" ") 
                dict[word[0]]= word[1]
                    
     
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                element = line.split(" ")
                for j in element:
                    if dict.has_key(j)== True:
                        g.write(j + " ")
                    else:
                        g.write("UNK" + " ")
                g.write("\n")
               

