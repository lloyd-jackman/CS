#This part opens up the original file and makes a dictionary, pairing the product_key field with the related_key field
rel_key = {}
for line in open('CH_LIP_STATISTICS.txt', 'r'):
    rel_key[line[0:8]] = line[-12:-4]
print(rel_key)


#This part opens the temp file in write mode, blanking previous contents, before closing it again and then 
open('CH_LIP_TER_Adj.txt', 'r')
open('temp_CS.txt', 'w')
open('temp_CS.txt', 'w').close()

#This part opens the hs5datafeeder output, goes through each line and adds the lookup of its product_key field to the next tab delimited column and another column with the value 18
for line in open('CH_LIP_TER_Adj.txt', 'r'):
    print(line[:-1] + '\t' + rel_key[line[0:8]] + "\t" + '18', file=open('temp_CS.txt', 'a'))

#This part closes the files used in the process
open('CH_LIP_STATISTICS.txt', 'r').close()
open('CH_LIP_TER_Adj.txt', 'r').close()
open('temp_CS.txt', 'a').close()

'''
This is the break between files for testing.
'''

# opening the new additional feed's contents
in_file = open('temp_CS.txt')
count_in = 0
for line in in_file:
    count_in = count_in + 1
print ('In file count:')
print(count_in)
print ('In file contents:')
print(open('in_file.txt').read())

# opening the original feed's file in read-mode and giving a line count
out_file = open('CH_LIP_STATISTICS.txt', 'r')
count_out = 0
for line in out_file:
    count_out = count_out + 1
print ('Out file line count:')
print (count_out)
print ('Out file contents:')
print(open('CH_LIP_STATISTICS.txt').read())
out_file.close()

# opening the original feed's file in append-mode and writing the in file to the end of it
out_file = open('CH_LIP_STATISTICS.txt', 'a')
out_file.write('\n')
out_file.write(open('temp_CS.txt').read())
out_file.close()

# opening the original feed's file in read-mode after appending 'indata' and giving a line count
out_file = open('CH_LIP_STATISTICS.txt', 'r')
count = 0
for line in out_file:
    count = count + 1
print ('out file post-process line count:', count)
print ('Out file contents, post-process:')
print(open('CH_LIP_STATISTICS.txt').read())

# tidying up
in_file.close()
out_file.close()


