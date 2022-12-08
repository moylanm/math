# coding: utf-8

import argparse, sys

CHAR_TO_NUM = {
  'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
  'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
  'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

NUM_TO_CHAR = {
  0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
  11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U',
  21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z',
}

MODULUS = 26

def translate_characters(s: str) -> list:
  return [CHAR_TO_NUM[x.upper()] for x in list(s)]

def translate_numbers(n: list) -> list:
  return [NUM_TO_CHAR[x] for x in n]

def encrypt(p: int, k: int) -> int:
  return (p + k) % MODULUS

def decrypt(p: int, k: int) -> int:
  return (p - k) % MODULUS

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  group = parser.add_mutually_exclusive_group()
  
  parser.add_argument('string', type=str, nargs='+')
  parser.add_argument('-k', '--key', type=int, required=True)
  group.add_argument('-d', '--decrypt', action='store_true')
  group.add_argument('-e', '--encrypt', action='store_true')
  
  args = parser.parse_args()
  
  if not args.encrypt and not args.decrypt:
    print('Must choose to encrypt or decrpyt.')
    sys.exit()
    
  result = []
  action = encrypt if args.encrypt else decrypt

  for s in args.string:
    result.append([action(p, args.key) for p in translate_characters(s)])
  
  print(' '.join([''.join(translate_numbers(c)) for c in result]))