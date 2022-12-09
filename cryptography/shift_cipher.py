# coding: utf-8

import sys, argparse, operator

class ShiftCipher:
  
  CHAR_TO_NUM = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
    'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
    'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
  }
  
  NUM_TO_CHAR = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
    11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U',
    21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'
  }
  
  MODULUS = 26
  
  def __init__(self, key: int) -> None:
    self.key = key
  
  def set_key(self, new_key: int):
    self.key = new_key
  
  def encrypt(self, text: str):
    return self._run(operator.pos, text)
  
  def decrypt(self, text: str):
    return self._run(operator.neg, text)
  
  def _run(self, op, text: str):
    translation = [self.CHAR_TO_NUM[c.upper()] if c.isalpha() else c for c in list(text)]
    
    for i in range(len(translation)):
      if isinstance(translation[i], int):
        translation[i] = self.NUM_TO_CHAR[(translation[i] + op(self.key)) % self.MODULUS]
         
    return ''.join(translation) # type: ignore

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  group = parser.add_mutually_exclusive_group()
  
  parser.add_argument('string', type=str, nargs='*', default=sys.stdin)
  parser.add_argument('-k', '--key', type=int)
  parser.add_argument('-b', '--brute-force', action='store_true')
  group.add_argument('-d', '--decrypt', action='store_true')
  group.add_argument('-e', '--encrypt', action='store_true')
  
  args = parser.parse_args()
  
  if not sys.stdin.isatty():
    args.string = args.string.read().replace('\n', '')
  elif isinstance(args.string, list):
    args.string = ' '.join(args.string)
  else:
    print('Need string to work with.')
    sys.exit()
  
  if args.brute_force:
    cipher = ShiftCipher(0)
    
    for n in range(26):
      print('{}: {}'.format(n, cipher.decrypt(args.string)))
      cipher.set_key(n + 1)
    
    sys.exit()
  
  if not args.encrypt and not args.decrypt:
    print('Must choose to encrypt or decrpyt.')
    sys.exit()
    
  if not args.key:
    print('Must choose to brute force or use key.')
    sys.exit()
  
  action = 'encrypt' if args.encrypt else 'decrypt'
  
  print(getattr(ShiftCipher(args.key), action)(args.string))