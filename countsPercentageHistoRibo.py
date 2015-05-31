import sys

def getCounts() :
    files=[]

    #Key = length, val = counts
    lenCounts={}
    for i in range(1,len(sys.argv)):
        files.append(sys.argv[i].rstrip())



    for fileName in files:
        readFile=open(fileName,"r")
        setFlag = False
        for line in  readFile:
            if setFlag == True:
                if not str(len(line.rstrip())) in lenCounts:
                    lenCounts[str(len(line.rstrip()))]=0
                lenCounts[str(len(line.rstrip()))]+=1
                
                setFlag = False
            if line[0] == "@":
                setFlag = True

    return lenCounts


def getPercentages(lenCounts):
    totals = 0.0
    for length in lenCounts:
        totals+=lenCounts[length]
        
    percentages = []    
    for length in lenCounts:
        percentages.append((int(length),lenCounts[length]/totals))
    percentages.sort()
    return percentages


if __name__ == "__main__":
    lenCounts = getCounts()
    percentages = getPercentages(lenCounts)
    outfile = open("outpCountsRibo","w")
    for line in percentages:
        outfile.write(str(line[0])+","+str(line[1])+"\n")
