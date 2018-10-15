
#!/usr/bin/env python
# coding=utf-8
with open("people-daily.txt") as f:
    with open("output.txt", "w") as d:
        readline =  f.readlines()
        for i in readline:
            strip = i.strip()
            split = strip.split(" ")
            for j in split:
                a = j.split("/")
                if a ==[""] or a[0].startswith("19980101") :
                    continue
            
                d.write(a[0] + "\t" +a[1] +"\n")
            d.write("\n")    
                  

