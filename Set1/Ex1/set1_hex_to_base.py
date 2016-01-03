#!/usr/bin/python -u
# -*- coding: utf-8 -*-

import re

'''
script as anwer to the matasano crypto challenges:
http://cryptopals.com/sets/1/challenges/1/ modified to module

Input: valid hex string

Output: base64 encoded input string
'''


str_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
str_hex_ = '737572652e'
decoded_str = []



def hext_to_base64(hex_str):
    #base64 character table
    base64_arr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    #prepare string - remove whitespace
    hex_str = hex_str.replace(" ", "")    
    #check if string is valid hex string
    ref = re.compile('[a-zA-Z0-9]', re.M)
    check = ref.match(str_hex)
    if check is None:
        print 'Provided hex string is not valid'
        sys.exit()
    else:
        continue
    
    pad_size = len(str_hex) % 3
    print pad_size
    str_hex_dec = [int(i, 16) for i in str_hex]
    print str_hex_dec

    for i in range (3, len(str_hex_dec) + (3 - pad_size), 3):
        print str_hex_dec[i-3], str_hex_dec[i-2], str_hex_dec[i-1]
        decoded_str.append(base64_arr[(str_hex_dec[i-3] << 2) | (str_hex_dec[i-2] >> 2)])
        decoded_str.append(base64_arr[(0x30 & (str_hex_dec[i-2] << 4)) | (str_hex_dec[i-1])])

    if pad_size == 2:
        decoded_str.append(base64_arr[(str_hex_dec[len(str_hex_dec)-2] << 2) | (str_hex_dec[len(str_hex_dec) -1] >> 2)])
        decoded_str.append(base64_arr[(str_hex_dec[len(str_hex_dec) - 1] << 2) & 0x20])
        decoded_str.append('==')
    if pad_size == 1:
        decoded_str.append(base64_arr[(str_hex_dec[len(str_hex_dec) - 1] << 2)]) 
        decoded_str.append('=')

    print ''.join(decoded_str)


#0x30 (00110000) 
#(0x30 & (str_hex[i-2] << 4)) | (str_hex[i-2])
#print len(str_hex)
#print str_hex_dec[0]
#print str_hex_dec.buffer_info()[1]
#print format(4, '#010b')
#get 3 chars:
#char

if __name__ == "__main__":
    print 'test'        
