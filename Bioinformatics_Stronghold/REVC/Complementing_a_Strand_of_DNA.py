# Complementing a Strand of DNA
# Problem Link: https://rosalind.info/problems/revc/

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'rosalind_revc.txt')

file= open(input_path,'r')
dna= file.read().replace("\n", "")
file.close()
dnac= dna[::-1]
dnaf= list(dnac)

i= 0
for n in dnac:
    if n== 'A':
        dnaf[i]= 'T'
    elif n== 'T':
        dnaf[i]= 'A'
    elif n== 'C':
        dnaf[i]= 'G'
    elif n== 'G':
        dnaf[i]= 'C'
    else:
        break
    i+=1

print(dna[0:5])
print(dnac[-5:])
print(''.join(dnaf[-5:]))

print(''.join(dnaf))