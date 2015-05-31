import sys

if len(sys.argv) < 2:
    print "usage: python getTranslationaleEfficiency.py <riboseqrpkM> <rnaSEQrpkM> <outp>"
    sys.exit()
    
riboInp = open(sys.argv[1], "r")

rnaInp = open(sys.argv[2],"r")

info = {}

for line in riboInp:
    fields=line.split("\t")
    if len(fields) == 3:
        info[fields[0].rstrip()] = (float(fields[1]),float(fields[2]))
        
outp = open(sys.argv[3],"w")

for line in rnaInp:
    fields=line.split("\t")
    if len(fields) == 3:
        if fields[0].rstrip() in info:
            if info[fields[0].rstrip()] [0] >= 5 and float(fields[1])>= 5:
                outp.write(fields[0].rstrip()+"\t"+str(info[fields[0].rstrip()] [1] / float(fields[2]))+"\n" )
     
