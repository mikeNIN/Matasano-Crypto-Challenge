#!/usr/bin/python -u
# -*- coding: utf-8 -*-

''' 
  function that xors two hex encoded strings (must be equal in lenght)
  
'''

def fixed_xor(str1, str2):
    #check if strings have equal len
    if len(str1) != len(str2):
        print 'length of given strings is not equal'
    
    xored = ''.join("{:x}".format(int(a, 16) ^ int(b, 16)) for a, b in zip(str1, str2))
     
    return xored
    
if __name__ == "__main__":
    str_1 = '1c0111001f010100061a024b53535009181c'
    str_2 = '686974207468652062756c6c277320657965'
    print fixed_xor(str_1, str_2)

