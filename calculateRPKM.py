import sys

def getRPKM(countsPerGene,total,geneSizes,outp):
    outFile = open(outp,"w")
    for gene in countsPerGene:
        rpkm = (1000000000*countsPerGene[gene])/(total*geneSizes[gene])
        outFile.write(gene+"\t"+str(rpkm)+"\t"+str(countsPerGene[gene])+"\n")
        

def getGeneSizes(infile):
    geneSizes={}
    sizeFile = open(infile,"r")
    for line in sizeFile:
        pairs = line.split("\t")
        if len(pairs) > 1:
            geneSizes[pairs[0]]=float(pairs[1].rstrip())
    return geneSizes    


def getCountsAndTotal(CountFiles):
    total = 0.0
    countsPerGene = {}
    print CountFiles
    for fileName in CountFiles:
        inp = open(fileName,"r")
        for line in inp:
            pairs = line.split("\t")
            if len(pairs) <= 1 or "__" in line:
                continue
            if not pairs[0] in countsPerGene:
                countsPerGene[pairs[0]]=0.0
            countsPerGene[pairs[0]]+=float(pairs[1].rstrip())
            total+=float(pairs[1].rstrip())
            
    print total
    return (countsPerGene,total)
            

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Usage: python calculateRPKM.py <geneSizeFile.txt> <CountFile1> <CountFile2> .....<outpFile>"
        sys.exit()
    geneSizes = getGeneSizes(sys.argv[1])
    
    countFiles = []
    for i in range(2,len(sys.argv)-1):
        countFiles.append(sys.argv[i].rstrip())
        
    countsPerGene,total = getCountsAndTotal(countFiles)
    getRPKM(countsPerGene,total,geneSizes,sys.argv[-1].rstrip())
     
    
