#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sunday Feb 10 19:02:37 2019

@author: Aishwarya
"""
def program(g,f):
    if g in f:
        return 1
    else:
        return 2
    
for a in range(0,11):
    for b in range(0,11):
        holding_place=[]
        for x in range(1,1001):
            x1=x
            f=[]
            c=0
            breaker=0
            p=[]
            while program(x1,f)==2:
                if c>1000:
                    breaker=1
                    print(a,b,'bad')
                    break;
                else:
                    f.append(x1)
                    if x1%2==0:
                        x1//=2
                    else:
                        x1=a*x1+b
                    c=c+1
            if(breaker==0):
                ndx=f.index(x1)
                p=f[ndx:]
                p.sort()
                if p not in holding_place and p != []:
                    holding_place.append(p)
            else:
                break
        if(breaker==0):
            plength=len(holding_place)
            print(a,b,plength)