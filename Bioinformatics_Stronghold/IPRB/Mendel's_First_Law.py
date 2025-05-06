# Mendel's First Law
# Problem Link: https://rosalind.info/problems/iprb/

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'rosalind_iprb.txt')

file= open(input_path,'r')
mendel= file.read().replace('\n','').split(' ')
mendel = list(map(int, mendel))

k = mendel[0]
m = mendel[1]
n = mendel[2]
total = k + m + n

# Probabilities for producing dominant offspring
kk = (k/total) * ((k-1)/(total-1))         # k x k → always dominant
km = (k/total) * (m/(total-1))             # k x m → always dominant
kn = (k/total) * (n/(total-1))             # k x n → always dominant
mk = (m/total) * (k/(total-1))             # m x k → always dominant
mm = (m/total) * ((m-1)/(total-1)) * 0.75  # m x m → 75% dominant
mn = (m/total) * (n/(total-1)) * 0.5       # m x n → 50% dominant
nk = (n/total) * (k/(total-1))             # n x k → always dominant
nm = (n/total) * (m/(total-1)) * 0.5       # n x m → 50% dominant

# Total probability
probability = kk + km + kn + mk + mm + mn + nk + nm

print(f'Probability that two randomly selected mating organisms will produce an individual possessing a dominant allele: {probability}')