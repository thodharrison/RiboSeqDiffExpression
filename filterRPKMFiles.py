import sys
'''
This script_creates a new filtered rpkM file based on what has been selected by edgeR
'''


if len(sys.argv) < 2:
    print" usage:\npython filterRPKMFiles.py <edgeR file> <rpkMfile> <Output file>"
    sys.exit()

edgeRInput = open(sys.argv[1],"r")
rpkMFile =open( sys.argv[2], "r")
output = open(sys.argv[3], "w")

keep = []

for line in edgeRInput:
    keep.append(line.split(",")[0])

for line in rpkMFile:
    if line.split("\t")[0] in keep:
        output.write(line)
output.close() 
