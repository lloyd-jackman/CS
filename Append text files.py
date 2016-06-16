# opening the new additional feed's contents
in_file = open('in_file.txt')
count_in = 0
for line in in_file:
    count_in = count_in + 1
print ('In file count:')
print(count_in)
print ('In file contents:')
print(open('in_file.txt').read())

# opening the original feed's file in read-mode and giving a line count
out_file = open('out_file.txt', 'r')
count_out = 0
for line in out_file:
    count_out = count_out + 1
print ('Out file line count:')
print (count_out)
print ('Out file contents:')
print(open('out_file.txt').read())
out_file.close()

# opening the original feed's file in append-mode and writing the in file to the end of it
out_file = open('out_file.txt', 'a')
out_file.write('\n')
out_file.write(open('in_file.txt').read())
out_file.close()

# opening the original feed's file in read-mode after appending 'indata' and giving a line count
out_file = open('out_file.txt', 'r')
count = 0
for line in out_file:
    count = count + 1
print ('out file post-process line count:', count)
print ('Out file contents, post-process:')
print(open('out_file.txt').read())

# tidying up
in_file.close()
out_file.close()
