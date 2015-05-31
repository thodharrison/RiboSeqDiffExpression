import sys,os

posFolder = sys.argv[1].rstrip()
negFolder = sys.argv[2].rstrip()
print posFolder
print negFolder
posFiles = os.listdir(posFolder)
negFiles = os.listdir(negFolder)

for i in range(len(posFiles)):
    for j in range(len(negFiles)):
        os.system("python scripts/plotRPKMCorrelation.py "+posFolder+"/"+posFiles[i]+" "+negFolder+"/"+negFiles[j]+" rpkMGraphs/"+posFiles[i]+"_"+negFiles[j]+".png")


