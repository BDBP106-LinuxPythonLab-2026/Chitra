#1
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

temps = np.arange(20, 71, 5)
activity = np.array([12, 20, 35, 52, 70, 85, 92, 78, 45, 18, 5])
fig, ax=plt.subplots()
ax.plot(temps,activity,marker="o")
ax.set_xlabel("Temperature(oC)")
ax.set_ylabel("Activity")
ax.set_title("Activity vs Temperature")

opt_temps=temps[np.argmax(activity)]
print("Optimum temperature",opt_temps)

ax.axvline(x=opt_temps,color='red',linestyle='--')
ax.annotate("Optimum Temperature = 50oC.", xy=(opt_temps,92))

plt.show()
#2
import numpy as np
import matplotlib.pyplot as plt
genes = ["GAPDH", "ACTB", "TP53", "MYC", "EGFR"]
control = np.array([950, 1200, 310, 150, 420])
treated = np.array([940, 1180, 610, 75, 430])
x=np.arange(len(genes))
width=0.4
fig,ax=plt.subplots()
ax.bar(x-width/2, control, width, label='Control')
ax.bar(x+width/2, treated, width, label='Treated')
ax.set_xlabel("Genes")
ax.set_ylabel("Expression level")
ax.set_title("Gene expression: Control vs Treated")
ax.set_xticks(x,labels=genes)
ax.legend()
plt.show()
fold_change=treated/control
print("Fold Change:")
for i in range(len(genes)):
    print(genes[i],":",round(fold_change[i],2))
#3
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(7)
length = rng.integers(50, 800, size=100) # amino acids
weight = length * 0.11 + rng.normal(0, 3, size=100) # kDa (about 110 Da per residue)
membrane = rng.random(100) < 0.3
fig,ax=plt.subplots()
ax.scatter(length[~membrane],weight[~membrane],color='blue',marker='o',alpha=0.5,label='Soluble proteins')
ax.scatter(length[membrane],weight[membrane],color='red',marker='^',alpha=0.5,label='Membrane proteins')
ax.set_xlabel("Protein length (amino acids)")
ax.set_ylabel("Molecular Weight (kDa)")
ax.set_title("Protein length vs Molecular weight")
ax.legend()
plt.savefig("protein_size.png",dpi=150)
#4
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(3)
organisms = ["E. coli", "S. cerevisiae", "P. falciparum", "S. coelicolor"]
mean_gc = [51, 38, 19, 72] # approximate genome GC content, %
fig,ax=plt.subplots(2,2,sharex=True,sharey=True)
#sharex=True means that all 4 plots have the same x-axis scale and sharey=True means that all 4 plots have the same y-axis scale.
bins=(np.arange(0,101,2))
for i in range(4):
    gc=rng.normal(mean_gc[i],4,size=1000)
    row=i//2
    col=i%2
    ax[row,col].hist(gc,bins=bins,color='skyblue')
    ax[row,col].axvline(mean_gc[i],color='red',linestyle='--')
    ax[row,col].set_title(organisms[i]+"(Mean="+str(mean_gc[i])+"%)")
ax[1,0].set_xlabel("GC Content(%)")
ax[1,1].set_xlabel("GC Content(%)")
ax[0,0].set_ylabel("Frequency")
ax[1,0].set_ylabel("Frequency")
fig.suptitle("Genome GC Content Distribution")
plt.tight_layout()
plt.show()
#5
import pandas as pd
df=pd.read_csv("diabetes.csv")
#(i)
print("Column names:")
print(df.columns)
#(ii)
print("First 10 rows:")
print(df.head(10))
#(iii)
print("Mean of Blood Pressure:")
print(df['BloodPressure'].mean())
#(iv)
print("First 4 rows of columns 3,4,5")
print(df.iloc[:4,2:5])
#(v)max-min normalization:
min_bp=df['BloodPressure'].min()
max_bp=df['BloodPressure'].max()
df['NormalizedBP']=(df['BloodPressure']-min_bp)/(max_bp-min_bp)
print("Normalized BP:")
print(df[['BloodPressure','NormalizedBP']])
#(vi)categorize age:
def categorize_age(age):
    if age>=1 and age<=18:
        return "Youth"
    elif age>=19 and age<=50:
        return "Adult"
    else:
        return "Senior"
df['AgeCategory']=df['Age'].apply(categorize_age)
print("Age Category:")
print(df[['Age','AgeCategory']])
#6
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-20,20,1000)
f1=np.log(1/np.cos(x)**2)
f2=np.log(1/np.sin(x)**2)
plt.plot(x,f1,label='f1(x)')
plt.plot(x,f2,label='f2(x)')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Logarithmic Trigonometric Functions")
plt.legend()
plt.show()
#7
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-6,6,1000)
sigma=[1,1.5,2]
for s in sigma:
    g=(1/(s*np.sqrt(2*np.pi)))*np.exp(-(x**2)/(2*s**2))
    plt.plot(x,g,label='sigma='+str(s))
plt.xlabel("x")
plt.ylabel("g(x)")
plt.title("Normalized Gaussian Functions")
plt.legend()
plt.show()
