# Solution 1

# Counting Point Mutations
# Problem Link: https://rosalind.info/problems/hamm/

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'rosalind_hamm.txt')

txt= open(input_path,'r')
file= txt.read().splitlines()
print(file)
txt.close()

i= 0
hamm= 0

while i<(len(file[0])):
    if file[0][i]!=file[1][i]:
        hamm+=1
    i+=1

print(hamm)

#%% 

# Solution 2

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'rosalind_hamm.txt')

with open(input_path) as file:
    lines= file.read().splitlines()

hamm= sum(a!=b for a,b in zip(lines[0],lines[1]))   
print(hamm) 