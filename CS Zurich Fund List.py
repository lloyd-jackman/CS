import os

# Clears the fund list file
open('t:\CS Zurich Fund List.txt', 'w')
open('t:\CS Zurich Fund List.txt', 'w').close()

# Writes Lipper IDs in file
count = 0
for line in open('\\\\Densgfdprod1\\ftpstaging\\datafeeds\\custom\\csuisse_ch\\CH_LIP_TER_Adj.txt', 'r'):
    if count == 0:
        count = count + 1
    else:
        print(line[0:8], file=open('CS Zurich Fund List.txt', 'a'))
        count = count + 1
