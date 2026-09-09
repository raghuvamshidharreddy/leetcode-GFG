class Solution:
     plusOne= lambda self, digits: [ int(j) for j in list(str(int(''.join(str(i) for i in digits))+1))]