
#!/usr/bin/python -u
# -*- coding: utf-8 -*-

base64_arr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
str_hex_ = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
str_hex = '61737572652e'
decoded_str = []

pad_size = len(str_hex) % 3

str_hex_dec = [int(i, 16) for i in str_hex]

for i in range (3, len(str_hex_dec) + (3 - pad_size), 3):
    decoded_str.append(base64_arr[(str_hex_dec[i-3] << 2) | (str_hex_dec[i-2] >> 2)])
    decoded_str.append(base64_arr[(0x30 & (str_hex_dec[i-2] << 4)) | (str_hex_dec[i-1])])


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
