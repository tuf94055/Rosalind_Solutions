# Counting DNA Nucleotides
# Problem Link: https://rosalind.info/problems/dna/

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'rosalind_dna.txt')

with open(input_path, 'r') as file:
    dna = file.read().strip()

A = dna.count('A')
C = dna.count('C')
G = dna.count('G')
T = dna.count('T')

print(A, C, G, T)