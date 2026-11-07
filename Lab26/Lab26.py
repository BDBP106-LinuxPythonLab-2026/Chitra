import numpy as np
from numpy import dtypes

#1
print(np.__version__)
#2(i)
a=np.arange(0,9)
print(a)
#2(ii)
c=np.array([[True,False,True],[False,True,False],[True,False,False]],dtype=bool)
print(c)
#2(iii)
d=np.arange(50)
prime=d[np.array([i>1 and all(i%j!=0 for j in range(2,i)) for i in d])]
print(prime)
#2(iv)
a=np.array([4,8,7,5,8,2,5,6,9,8,4,5,5,3,2,5,6,4,5,2])
print(a)
new=a.reshape(4,5)
print(new)
#2(v)

a=np.arange(9)
b=np.ones(9)
print(a)
print(b)
new=np.hstack((a,b))
print(new)
#2(vi)
a=np.arange(101)
prime=a[np.array([i>1 and all(i%j!=0 for j in range(2,i)) for i in a])]
new=np.intersect1d(a,prime)
print(new)
#2(vii)
new=np.setdiff1d(a,prime)
print(new)
#2(viii)
new=np.where(np.isin(a,prime))
print(new)
#2(ix)
new=a[(a>5) & (a<20)]
print(new)
#3
a=np.arange(12).reshape((2,2))
print(a)
row=(a[::-1])
print(row)
col=(a[:,::-1])
print(col)
#4
import numpy as np
arr=np.random.randint(1,100,(3,3))
print("Original matrix:")
print(arr)
arr[:,[0,1]]=arr[:,[1,0]]
print("After swapping:")
print(arr)
#5
import numpy as np
def maximum(a,b):
    c=np.maximum(a,b)
    return c
a=np.array([1,2])
b=np.array([0,5])
c=maximum(a,b)
print(c)
#6
import numpy as np
np.set_printoptions(precision=3)
arr=np.random.rand(3,3)
print(arr)
#7
import numpy as np
np.set_printoptions(suppress=True)
arr=np.array([1000000,2000000,3000000])
print(arr)
#8
import numpy as np
arr=np.array([10,25,30,15,40,50,5,60,18,35])
print("Average:",np.mean(arr))
print("Highest:",np.max(arr))
print("Lowest:",np.min(arr))
print("Numbers above 20:", np.sum(arr>20))
print("Numbers below 20:", arr[arr<20])
#9
import numpy as np
counts=np.array([100,200,400,800,1600])
log_values=np.round(np.log2(counts),2)
percentage=np.round((counts/np.sum(counts))*100,1)
print("Gene Counts:")
print(counts)
print("Log2 Values:")
print(log_values)
print("Percentage:")
print(percentage)
#10
import numpy as np
t=np.arange(0,121,20)
population=100*2**(t/20)
print("Time:",t)
print("Population:",population)
print("Final population is:",population[-1]/population[0],"times larger")
print("Time points where population is above 1000:",t[population>1000])
#11
import numpy as np
seq="GATTACA"
encoding={'A':[1,0,0,0],'C':[0,1,0,0],'G':[0,0,1,0],'T':[0,0,0,1]}
arr=[]
for base in seq:
    arr.append(encoding[base])
result=np.array(arr)
print("DNA Sequence:",seq)
print("One hot encoding:")
print(result)
#12
import numpy as np
arr=np.random.rand(5,10)*100
print("Original gene expression:")
print(arr)
mean=np.mean(arr,axis=1,keepdims=True)
normalized=arr-mean
print("Normalized expression:")
print(normalized)
sample_sum=np.sum(normalized,axis=0)
print("Sample sums:")
print(sample_sum)
threshold=50
print("Samples above threshold:")
print(np.where(sample_sum>threshold)[0]+1)
