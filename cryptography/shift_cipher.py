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
  
  def __init__(self, key: int, modulus: int = 26) -> None:
    self.modulus = modulus
    self.key = key
  
  def encrypt(self, text: str):
    return self._run(operator.pos, text)
  
  def decrypt(self, text: str):
    return self._run(operator.neg, text)
  
  def _run(self, op, text: str):
    translation = [self.CHAR_TO_NUM[c.upper()] if c != ' ' else c for c in list(text)]
    
    for i in range(len(translation)):
      if isinstance(translation[i], int):
        translation[i] = self.NUM_TO_CHAR[(translation[i] + op(self.key)) % self.modulus]
         
    return ''.join(translation) # type: ignore

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  group = parser.add_mutually_exclusive_group()
  
  parser.add_argument('string', type=str, nargs='*', default=sys.stdin)
  parser.add_argument('-k', '--key', type=int, required=True)
  group.add_argument('-d', '--decrypt', action='store_true')
  group.add_argument('-e', '--encrypt', action='store_true')
  
  args = parser.parse_args()
  
  if not args.encrypt and not args.decrypt:
    print('Must choose to encrypt or decrpyt.')
    sys.exit()
    
  if not sys.stdin.isatty():
    args.string = args.string.read().replace('\n', '')
  elif isinstance(args.string, list):
    args.string = ' '.join(args.string)
  else:
    print('Need string to work with.')
    sys.exit()
    
  cipher = ShiftCipher(args.key)
  action = 'encrypt' if args.encrypt else 'decrypt'
  
  print(getattr(cipher, action)(args.string))