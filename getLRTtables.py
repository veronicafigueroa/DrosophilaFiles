# Making appropriate R-compatible table for genes of interest
# Gene      11th_omega      lnL0        lnL0        LRT


import os

os.chdir('/Users/lalaf/PycharmProjects/InterestGenesLRT/Model78Txt')
list_of_files = os.listdir('/Users/lalaf/PycharmProjects/InterestGenesLRT/Model78Txt')

header_list = ['Gene', '11th Omega', 'Omega > 1?', 'lnL0', 'lnL1', 'LRT', 'Chi-Squared Significant?']
with open('PleiInterestTable', 'w') as f:
    for header in header_list:
        f.write("{:^25}".format(header))
    f.write("\n")

for file in list_of_files:
    read_file = open(file, 'r')
    input_list = read_file.readlines()

    output_list = []

    # gene name
    file_name = file.split("_")[2]
    output_list.append(file_name)

    # for each individual line in file
    class11 = 0;
    for line in input_list:
        if class11 == 3:
            w = line.split()[-1]
            output_list.append(w)

            # is omega > 1
            if float(w) > 1:
                output_list.append("Yes")
            else:
                output_list.append("No")
            class11 = 0;
        elif class11 == 2:
            class11 = class11 + 1
        elif class11 == 1:
            class11 = class11 + 1
        elif "MLEs of dN/dS (w) for site classes (K=11)" in line:
                class11 = class11 + 1

    #11th gene thing
    for line in input_list:
        # lnL vals
        if "lnL" in line:
            # this gets actual value
            lnL = line.split()[4]
            output_list.append(lnL)

    # get LRT
    LRT = 2 * (float(output_list[-1]) - float(output_list[-2]))
    output_list.append(str(LRT))

    if LRT >= 5.991:
        output_list.append("Yes")
    else:
        output_list.append("No")

    # writing to output table
    with open('PleiInterestTable', 'a') as f:
        for index in output_list:
            f.write("{:^25}".format(index))
        f.write("\n")
