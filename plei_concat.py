# Author: Veronica Figueroa
# Date  : 10/19/2022
# Description: Looping through all fasta files and concatenating genes for all 6 species (or adding
# appropriate number of dashes

import os
from Bio import SeqIO

# fill!!


# Set-up
totalLen = 0 # total length of final alignment
seqLenList = [] # list of sequence lengths
numGenes = 0 # number of genes in folder

 # Empty strings for each species
DsimSeq = ""
DsecSeq = ""
DmelSeq = ""
DyakSeq = ""
DercSeq = ""
DanaSeq = ""


#global variables

OUTPUT_NAMES = ["Drosophila_simulans", "Drosophila_sechellia", "Drosophila_melanogaster",
                "Drosophila_yakuba", "Drosophila_erecta", "Drosophila_ananassae"]


# loop through all fasta files in each folder
for filename in os.listdir():
    if filename.endswith(".fasta"):
        ++numGenes
        seqDict = SeqIO.to_dict(SeqIO.parse(filename, "fasta"))

        # get length of alignment by pulling out one of the dictionary entries (doesn't matter which one)
        firstKey = list(seqDict.keys())[0]
        firstSeq = str(seqDict[firstKey].seq)
        seqLen = len(firstSeq)
        totalLen = totalLen + seqLen
        seqLenList.append(seqLen)

        # look for Dana in seqdict
        searchkey = "Drosophila_simulans"
        res = [val for key, val in seqDict.items() if searchkey in key]
        if res != []:  # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqDict[resid].seq)
            DsimSeq = DsimSeq + resseq
        else:  # if res is empty
            emptyseq = "-" * seqLen
            DsimSeq = DsimSeq + emptyseq
            # look for Dana in seqdict

        searchkey = "Drosophila_sechellia"
        res = [val for key, val in seqDict.items() if searchkey in key]
        if res != []:  # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqDict[resid].seq)
            DsecSeq = DsecSeq + resseq
        else:  # if res is empty
            emptyseq = "-" * seqLen
            DsecSeq = DsecSeq + emptyseq

        searchkey = "Drosophila_melanogaster"
        res = [val for key, val in seqDict.items() if searchkey in key]
        if res != []:  # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqDict[resid].seq)
            DmelSeq = DmelSeq + resseq
        else:  # if res is empty
            emptyseq = "-" * seqLen
            DmelSeq = DmelSeq + emptyseq

        searchkey = "Drosophila_yakuba"
        res = [val for key, val in seqDict.items() if searchkey in key]
        if res != []:  # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqDict[resid].seq)
            DyakSeq = DyakSeq + resseq
        else:  # if res is empty
            emptyseq = "-" * seqLen
            DyakSeq = DyakSeq + emptyseq

        searchkey = "Drosophila_erecta"
        res = [val for key, val in seqDict.items() if searchkey in key]
        if res != []:  # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqDict[resid].seq)
            DercSeq = DercSeq + resseq
        else:  # if res is empty
            emptyseq = "-" * seqLen
            DercSeq = DercSeq + emptyseq

        searchkey = "Drosophila_ananassae"
        res = [val for key, val in seqDict.items() if searchkey in key]
        if res != []:  # if res is not empty:
            resid = str(res).split(",")[2]
            resid = resid.split("=")[1]
            resid = resid.split("'")[1]
            resseq = str(seqDict[resid].seq)
            DanaSeq = DanaSeq + resseq
        else:  # if res is empty
            emptyseq = "-" * seqLen
            DanaSeq = DanaSeq + emptyseq

# write new file name
newfile = open("plei_concat", "w")

SEQ_NAMES = [DsimSeq, DsecSeq, DmelSeq, DyakSeq, DercSeq, DanaSeq]
for outName, seqName in zip(OUTPUT_NAMES, SEQ_NAMES):
    newfile.write(">" + outName + "\n")
    newfile.write(seqName + "\n")
newfile.close()
