#!/usr/bin/env python
from random import randint
s=1
reach=int(raw_input())
randomnum=[]
for _ in range(reach):
    randomnum.append(randint(0,20))
print randomnum
while s:
    s=0
    for var in range(1,reach):
        if randomnum[var-1]>randomnum[var]:
            t1=randomnum[var-1]
            t2=randomnum[var]
            randomnum[var-1]=t2
            randomnum[var]=t1
            s=1
print randomnum
