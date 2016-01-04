#!/usr/bin/python -u
# -*- coding: utf-8 -*-

import re

'''
script as anwer to the matasano crypto challenges:
http://cryptopals.com/sets/1/challenges/1/ modified to module
Input: hex string () (ie. 4d not 0x4d)
Output: base64 encoded input string

written by Michal Freygant 04-01-2016
'''


def hext_to_base64(hex_str):
    #base64 character table
    
    #prepare string - remove whitespace and turn to lower
    hex_str = hex_str.replace(" ", "").lower()
    
    #check if string is valid hex string
    ref = re.compile('^[a-f0-9]+$', re.M)
    check = ref.search(str_hex)
    
    if check is None:
        print 'Provided string is not valid hex string'
        return 
    else:
        pad_size = len(str_hex) % 3
        str_hex_dec = [int(i, 16) for i in str_hex]
        decoded_str = []
        base64_arr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    #continue
    
    for i in range (3, len(str_hex_dec) + (3 - pad_size), 3):
        #print str_hex_dec[i-3], str_hex_dec[i-2], str_hex_dec[i-1]
        decoded_str.append(base64_arr[(str_hex_dec[i-3] << 2) | (str_hex_dec[i-2] >> 2)])
        decoded_str.append(base64_arr[(0x30 & (str_hex_dec[i-2] << 4)) | (str_hex_dec[i-1])])

    if pad_size == 2:
        decoded_str.append(base64_arr[(str_hex_dec[len(str_hex_dec)-2] << 2) | (str_hex_dec[len(str_hex_dec) -1] >> 2)])
        decoded_str.append(base64_arr[(str_hex_dec[len(str_hex_dec) - 1] << 2) & 0x20])
        decoded_str.append('==')
    if pad_size == 1:
        decoded_str.append(base64_arr[(str_hex_dec[len(str_hex_dec) - 1] << 2)]) 
        decoded_str.append('=')

    return ''.join(decoded_str)
    
if __name__ == "__main__":
    str_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print hext_to_base64(str_hex)
    
