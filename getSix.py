# author: Veronica Figueroa
# Date: 9/17/2022
# Purpose: Script to filter only desired organisms and print gene sequences to new fasta file

from Bio import SeqIO
import os


# global const list of desired species names
DESIRED_SPEC = ['Dsim', 'Dsec', 'Dmel', 'Dyak', 'Derc', 'Dana']

# get all desired files
os.chdir('/Users/lalaf/PycharmProjects/Drosophila/seqfiles_pleiotropic_genes_edited/originals')
list_of_files = os.listdir('/Users/lalaf/PycharmProjects/Drosophila/seqfiles_pleiotropic_genes_edited/originals')

for file in list_of_files:
    # read in fasta file as dictionary
    seq_dict = SeqIO.to_dict(SeqIO.parse(file, "fasta"))

    # create new dictionary for output
    output_dict = {}


    # record only desired files in new dictionary
    for record in seq_dict:
        x = record.split("_")[0]
        if x in DESIRED_SPEC:
            if x == 'Dsim':
                x = 'Drosophila_simulans'
            elif x == 'Dsec':
                x = 'Drosophila_sechellia'
            elif x == 'Dmel':
                x = 'Drosophila_melanogaster'
            elif x == 'Dyak':
                x = 'Drosophila_yakuba'
            elif x == 'Derc':
                x = 'Drosophila_erecta'
            elif x == 'Dana':
                x = 'Drosophila_ananassae'
            output_dict[x] = seq_dict[record]
            output_dict[x].id = x
            output_dict[x].description = x

    # create new files name
    file_name = file.split(".")
    output_file = file_name[0] + "_updated." + file_name[1]

    os.chdir('/Users/lalaf/PycharmProjects/Drosophila/seqfiles_pleiotropic_genes_edited/originals_updated')
    # print desired to new fasta files
    (SeqIO.write(output_dict.values(), output_file, 'fasta-2line'))

    #revert back to original folder
    os.chdir(
        '/Users/lalaf/PycharmProjects/Drosophila/seqfiles_pleiotropic_genes_edited/originals')