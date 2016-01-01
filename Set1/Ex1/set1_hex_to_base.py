#!/usr/bin/python -u
# -*- coding: utf-8 -*-

base64_arr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
str_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
str_hex_ = '737572652e'
decoded_str = []

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

if __name__ == "__main__":
    print 'test'        
