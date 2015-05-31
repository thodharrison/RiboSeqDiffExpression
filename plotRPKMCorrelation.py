

import sys,os
import rpy2.robjects as ro

leftFile = open(sys.argv[1].rstrip(),"r")
rightFile = open(sys.argv[2].rstrip(),"r")
outfile = open("forRGraph.csv","w")
logFile = open("log.txt","a")
outfile.write("Gene,PosRPKM,NegRPKM\n")
graphFile=sys.argv[3]
geneRPKMS = {}

for line in leftFile:
    lineVec = line.split("\t")
    if not len(lineVec) <= 1:
         geneRPKMS[lineVec[0]]=[]
         if float(lineVec[1].rstrip())==0:
             geneRPKMS[lineVec[0]].append("0.0001")
         else:
             geneRPKMS[lineVec[0]].append(lineVec[1].rstrip())
         geneRPKMS[lineVec[0]].append(float(lineVec[2].rstrip()))
         
         
for line in rightFile:
    lineVec = line.split("\t")
    if not len(lineVec) <= 1:
         if float(lineVec[1].rstrip())==0:
             geneRPKMS[lineVec[0]].append("0.0001")
         else:
             geneRPKMS[lineVec[0]].append(lineVec[1].rstrip())
    geneRPKMS[lineVec[0]].append(float(lineVec[2].rstrip()))
         
for key in geneRPKMS:
    if float(geneRPKMS[key][1]) >= 5 and float(geneRPKMS[key][3]) >= 5:
        #print key+","+geneRPKMS[key][0]+","+geneRPKMS[key][2]+"\n"
        outfile.write(key+","+geneRPKMS[key][0]+","+geneRPKMS[key][2]+"\n")
outfile.close()
MockName = ""

if "-2" in sys.argv[1]:
    MockName = "Mock Rep 1"
elif "-4" in sys.argv[1]:
    MockName = "Mock Rep 2"
elif "-1" in sys.argv[1]:
    MockName = "Mock Rep 3"        
elif "-3" in sys.argv[1]:
    MockName = "Mock Rep 4"       
elif "+1" in sys.argv[1]:
    MockName = "IAA Rep 1"
elif "+2" in sys.argv[1]:
    MockName = "IAA Rep 2"
elif "+3" in sys.argv[1]:
    MockName = "IAA Rep 3" 
elif "+5" in sys.argv[1]:
    MockName = "IAA Rep 4"
   
AuxName=""
if "+1" in sys.argv[2]:
    AuxName = "IAA Rep1"
elif "+2" in sys.argv[2]:
    AuxName = "IAA Rep 2"
elif "+3" in sys.argv[2]:
    AuxName = "IAA Rep 3" 
elif "+5" in sys.argv[2]:
    AuxName = "IAA Rep 4"
elif "-2" in sys.argv[2]:
    AuxName = "Mock Rep 1"
elif "-4" in sys.argv[2]:
    AuxName = "Mock Rep 2"
elif "-1" in sys.argv[2]:
    AuxName = "Mock Rep 3"        
elif "-3" in sys.argv[2]:
    AuxName = "Mock Rep 4"            
print AuxName
print MockName
             
ro.r("rpkm = read.csv('forRGraph.csv',header=TRUE)")
ro.r('png(filename="'+graphFile+'")')
ro.r('reg1 <- lm(log10(rpkm$NegRPKM)~log10(rpkm$PosRPKM))')
ro.r('rsq = summary(reg1)$adj.r.squared')
#ro.r('print(str(rsq))')
ro.r('plot(rpkm$PosRPKM, rpkm$NegRPKM, xlab="'+AuxName+' ", ylab="'+MockName+'", pch=19, log = "xy")')
ro.r('abline(reg1,col="red")')
ro.r('legend("topleft", bty="n", legend= bquote(R^2~ .(round(rsq,4))))')
ro.r('dev.off()')   
logFile.write(AuxName+"_"+MockName+","+str(ro.r('round(summary(reg1)$adj.r.squared,4)'))+"\n")
os.remove("forRGraph.csv")         
