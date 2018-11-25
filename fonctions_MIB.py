# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:49:31 2018

@author: titou
"""
from MaBase_MIB import*

def lettre(gardien,aliment):
    if gardien[0]==aliment[0]:
        n='oui'
    else:
        n='non'
    return(n)
    
    
def autre(gardien,aliment):
    return( gardien[0]==aliment[0])
       
   