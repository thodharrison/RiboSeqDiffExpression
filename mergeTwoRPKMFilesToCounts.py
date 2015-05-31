import sys
import os
# This merges two rpkm files to get a bradf new one
if len( sys.argv) < 2:
    print" usage: python mergeTwoRPKMFiles.py <rpkm1> <rpkm2> <gene size file> <outp>"
    sys.exit()
    
rpkmFileOne = open(sys.argv[1],"r")
rpkmFileTwo =open( sys.argv[2], "r")
gsf = sys.argv[3]
outp = sys.argv[4]
    
    
countDict={}
for line in rpkmFileOne:
    countDict[line.split("\t")[0]] = int(float(line.split("\t")[-1].rstrip()))
for line in rpkmFileTwo:
    countDict[line.split("\t")[0]] += int(float(line.split("\t")[-1].rstrip()))
    
tempCount = open("temp.txt","w")
for key in countDict:
    tempCount.write(key+"\t"+str(countDict[key])+"\n")
tempCount.close()
os.system("python scripts/calculateRPKM.py "+gsf+  " temp.txt "+ outp)
os.remove("temp.txt")        
