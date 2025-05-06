# Transcribing DNA into RNA
# Problem Link: https://rosalind.info/problems/rna/

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'rosalind_rna.txt')

file= open(input_path,'r')
rna= file.read()

rna_new= rna.replace('T','U')

print(rna_new)