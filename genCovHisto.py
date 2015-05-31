import sys
import rpy2.robjects as ro

if len(sys.argv)==1:
    print "title color(R|B) infile outfile startpos end pos"
    sys.exit()
    
title = sys.argv[1]
color = sys.argv[2]
infile = open(sys.argv[3],"r")
outfile = sys.argv[4]
startPos = int (sys.argv[5])
endPos = int(sys.argv[6].rstrip())

tempCsv = open("temp.csv","w")
tempCsv.write("Pos,Depth\n")

covDic = {}
for line in infile:
    vec = line.split("\t")
    if len(vec) > 2:
        #print vec[1]
        covDic[int(vec[1])] = vec[2].rstrip()
        
for i in range(startPos,endPos+1):
    if i in covDic:
       tempCsv.write(str(i-startPos)+","+covDic[i]+"\n")
    else:
       tempCsv.write(str(i-startPos)+",0\n") 
       
colToUse = "blue"       
if color == "R":
    colToUse = "red"
                  
ro.r('pdf("'+outfile+'")')
ro.r('data = read.csv("temp.csv",header =TRUE)')
ro.r('plot(data$Pos, data$Depth, type ="h", main = "'+title+'", xlab = "Position", ylab = "Depth",col = "'+colToUse+'" )')
ro.r('dev.off()')
