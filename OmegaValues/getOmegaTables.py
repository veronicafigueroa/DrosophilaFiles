# Author: Veronica Figueroa
# Date: 10/06/2022
# Details: Parse omega outputs to R-compatible tables

import os

os.chdir('/Users/lalaf/PycharmProjects/DrosophilaOmega/OmegaValues')
list_of_files = os.listdir('/Users/lalaf/PycharmProjects/DrosophilaOmega/OmegaValues')

# global variable of 3 group names
FILE_NAMES = ['plei', 'nonplei', 'devo']

# read in each text file of omega values (one for each gene group)
for file in list_of_files:
    read_file = open(file, 'r')
    input_list = read_file.readlines()

    omega_val_list = []

    # for each individual line in file
    for line in range(len(input_list)):
        name = (input_list[line].split('_'))[2]
        value = (input_list[line].split('= '))[1]
        omega_val_list.append(name + '     ' + value)

    # set up proper file name for each group
    name = ''
    if FILE_NAMES[1] in file:
        name = FILE_NAMES[1]
    elif FILE_NAMES[0] in file:
        name = FILE_NAMES[0]
    else:
        name = FILE_NAMES[2]

    # write results to new file
    with open(name + '_Omega_Table', 'w') as f:
        for index in omega_val_list:
            f.write(index)
