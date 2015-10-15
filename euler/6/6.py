d = 0
sumsq = 0
sqsum = 0
for i in range (0, 101):
    sumsq += i*i
    sqsum += i
sqsum = sqsum*sqsum

print sqsum - sumsq

