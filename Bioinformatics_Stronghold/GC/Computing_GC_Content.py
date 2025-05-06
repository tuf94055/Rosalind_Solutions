# Computing GC Content
# Problem Link: https://rosalind.info/problems/gc/

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'rosalind_gc.txt')

txt= open(input_path,'r')
fasta= txt.read().splitlines()
txt.close()
print(fasta)

IDs= []
GCs= []
AT= 0
GC= 0

for x in fasta:
    if x[0]=='>':
        IDs.append(x)
        if GC+AT==0:
            continue
        else:
            GCs.append(GC/(AT+GC))
        AT= 0
        GC= 0
    else:
        for y in x:
            if y== 'C' or y== 'G':
                GC+=1
            else:
                AT+=1
    
GCs.append(GC/(AT+GC))

fratio=0
i=-1

for z in GCs:
    i+=1
    if z>fratio:
        fratio= z
        fi=i

print(IDs[fi].replace('>',''),str(GCs[fi]*100)+'%')