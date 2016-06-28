input = raw_input()
n = input.split(" ")[0]
k = input.split(" ")[1]

n = int(n)
k = int(k)

if k >= n:
    print 2
else:
    print (2*n+k-1)/k
