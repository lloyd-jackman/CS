rel_key = {}
for line in open('CH_LIP_STATISTICS.txt', 'r'):
    rel_key[line[0:8]] = line[-12:-4]
#     print (line[0:8] + ' ' + line[-12:-4])
print(rel_key)


open('CH_LIP_TER_Adj.txt', 'r')
open('CH_LIP_TER_Adj.txt', 'r').close()

open('temp_CS.txt', 'w')

for line in open('CH_LIP_TER_Adj.txt', 'r'):
    print(line[:-1] + '\t' + rel_key[line[0:8]] + "\t" + '18', file=open('temp_CS.txt', 'a'))

open('CH_LIP_STATISTICS.txt', 'r').close()
open('CH_LIP_TER_Adj.txt', 'r').close()



