import string
import sys
import argparse
import logging
import codecs
import os
import time
from operator import itemgetter
from datetime import datetime
import re

#global variables
base_list= [line.rstrip() for line in open('../big-bases/base-2048.txt')]
base=len(base_list)

b58_digits = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
#end of global variables



digs = list(string.digits + string.lowercase)

def int2base(x, base, joiner='-'):
  if x < 0: sign = -1
  elif x==0: return '0'
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(base_list[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return joiner.join(digits)

def base58toint(input_base58):
  n = 0
  for c in input_base58:
    n *= 58
    if c not in b58_digits:
        raise InvalidBase58Error('Character %r is not a valid base58 character' % c)
    digit = b58_digits.index(c)
    n += digit
    print(n)
    return(n)
#int2base(10,360)



# convert address to long number

#__b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
#__b58base = len(__b58chars)
#long_value = 0
#for (i, c) in enumerate('bitcoin-address'[::-1]):
#long_value += __b58chars.find(c) * (__b58base**i)

