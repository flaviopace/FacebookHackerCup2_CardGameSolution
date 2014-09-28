import sys
import math
from collections import Counter
import re
import itertools
 
in_file = open(sys.argv[1],"r")
exp = in_file.read()
in_file.close()
 
 
 
inputFile= exp.split("\n")
 
 
 
 
index=[]
values=[]
 
def findsubsets(S,m):
 return set(itertools.combinations(S, m))
a=[]
flavio=1
for i in range(1, len(inputFile)-1) :
 values=[]
 allsub=[]
 if(i%2) :
# index.append(inputFile[i])
 n,k=map(int,inputFile[i].split())
 else :
 
 values= map(int,inputFile[i].split())
 
 # Optimization , not call a function
 allsub=itertools.combinations(values,k)
 
 my_sum=0
 
for f in allsub:
 
 my_max=max(f)
 my_sum += (my_max)
 
 if(my_sum>=1000000007):
 my_sum = my_sum -1000000007
 
print "Case #"+str(flavio)+": "+str(my_sum)
 
flavio +=1
