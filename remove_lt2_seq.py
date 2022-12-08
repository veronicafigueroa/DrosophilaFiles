# author: Veronica Figueroa
# Date: 9/22/2022
# Purpose: Filter out files with <2 sequences into new folder

# if >2 sequences, filter out into new folder
#os.remove

from Bio import SeqIO
import os
import shutil
# wrong dir!!!

os.chdir('/Users/lalaf/PycharmProjects/Drosophila/seqfiles_developmental_genes_edited/originals_updated')
list_of_files = os.listdir('/Users/lalaf/PycharmProjects/Drosophila/seqfiles_developmental_genes_edited/originals_updated')

for file in list_of_files:
    # read in fasta file as dictionary
    seq_dict = SeqIO.to_dict(SeqIO.parse(file, "fasta"))

    if len(seq_dict) < 2:
        shutil.move(file, '/Users/lalaf/PycharmProjects/Drosophila/seqfiles_developmental_genes_edited/originals_updated_not_enough_seqs')

