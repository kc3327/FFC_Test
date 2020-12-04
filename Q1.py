# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 19:35:08 2020

@author: Aaron
"""

N=32434567
def OrderedDeck_Brut(n):#Brutal Force
    l=list(range(1,n+1))#Generate the list from 1 to n
    while len(l)>=2:#End the game only when the number of the deck is less than one
        l.pop(0)    #Discard the first card
        l=l[1:]+[l[0]] #Move the second card to the bottom of the deck
    return l[0] #Return the only card left
# print(OrderedDeck_Brut(N))


def OrderedDeck_Half(n):# Faster than Brutal Force
    l=list(range(1,n+1))#Generate the list from 1 to n
    while len(l)>=2:#End the game only when the number of the deck is less than one
        if len(l)%2==0:#If the remaining list contains even elements
            l=[l[i] for i,x in enumerate(l) if i%2 !=0]# remove the odd th number(even index)
        else:
            l=[l[i] for i,x in enumerate(l) if i%2 !=0]# remove the odd th number(even index)
            l=l[1:]+[l[0]]#Move the first element to the bottem of the deck
    return l[0]
# print(OrderedDeck_Half(N))


import math
def OrderedDeck_Closed(n):# Fastest among these three functions
    return 2 * (n -  (2 ** (ceil(math.log(n,2))-1)))
print(OrderedDeck_Closed(N))
