with open("27_b.txt") as F:
  N = int( F.readline() )
  data = [ int(F.readline()) for i in range(N) ]

K = 43

tailSum = [0] + [None]*(K-1)
tailLen = [0]*K
maxSum, minLen = 0, 0
totalSum = 0

for i in range(N):
  totalSum += data[i]
  r = totalSum % K
  if tailSum[r] != None:
    curSum = totalSum - tailSum[r]
    curLen = i - tailLen[r]
    if curSum > maxSum or \
       (curSum == maxSum and curLen < minLen):
      maxSum = curSum
      minLen = curLen
  else:
    tailSum[r] = totalSum
    tailLen[r] = i
print( minLen )
