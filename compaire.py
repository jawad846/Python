f1=open("/home/jawad/Documents/waf.txt","r")
f2=open("/home/jawad/Documents/IP.txt","r")
for line1 in f1:
    for line2 in f2:
        if line1==line2:
            print("SAME\n")
        else:
            print("Not Same")
        break
f1.close()
f2.close()