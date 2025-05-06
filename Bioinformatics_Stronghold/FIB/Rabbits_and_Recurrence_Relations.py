# Rabbits and Recurrence Relations
# Problem Link: https://rosalind.info/problems/fib/

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'rosalind_fib.txt')

txt= open(input_path,'r')
fib= txt.read().replace('\n','').split(' ')

n= int(fib[0])
k= int(fib[1])

i= 1
rabbits= [1,0]

print(rabbits)

while i!=n:
    C= rabbits[0]
    A= rabbits[1]
    rabbits[1]+=C
    rabbits[0]-=C
    rabbits[0]+= k*A
    i+=1
    print(i, rabbits)
    
print('Final rabbit count: ', sum(rabbits))