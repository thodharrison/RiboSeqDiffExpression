import sys

inp = open(sys.argv[1],"r")
outp=open(sys.argv[2],"w")

genePos={}
prevLine = "notAGene"
for line in inp:
    lineVec = line.split("\t")
    if len (lineVec) <=1:
        continue
    gene = lineVec[8].split("\"")[1]
    if not gene in genePos:
        genePos[gene]=[]
    genePos[gene].append(int(lineVec[3]))
    genePos[gene].append(int(lineVec[4]))
    
for gene in genePos:
    print 
    outp.write(gene+"\t"+str((max(genePos[gene])-min(genePos[gene])+1))+"\n")
