# coding: utf-8

import sys, argparse

class AffineCipher:
  
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
  
  def __init__(self, a: int, b: int) -> None:
    self.a = a
    self.b = b
    
  def encrypt(self, text: str):
    return self._run(lambda p: (self.a * p + self.b), text)
  
  def decrypt(self, text: str):
    a_inverse = self._a_inverse()
    return self._run(lambda p: a_inverse * (p - self.b), text)

  def _run(self, op, text: str):
    translation = [self.CHAR_TO_NUM[c.upper()] if c.isalpha() else c for c in list(text)]
    
    for i in range(len(translation)):
      if isinstance(translation[i], int):
        translation[i] = self.NUM_TO_CHAR[op(translation[i]) % self.MODULUS]

    return ''.join(translation) # type: ignore

  def _a_inverse(self):
    '''
    Extended Euclidean Algorithm Adaptation
    Credit: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    '''
    t, new_t = 0, 1
    r, new_r = self.MODULUS, self.a
    
    while new_r != 0:
      quotient = r // new_r
      t, new_t = new_t, t - quotient * new_t
      r, new_r = new_r, r - quotient * new_r
      
    if r > 1:
      raise Exception('a ({}) is not invertible'.format(self.a))
    if t < 0:
      t = t + self.MODULUS
      
    return t
    
def gcd(a: int, b: int = 26):
  x, y = a, b
  
  while y != 0:
    r = x % y
    x = y
    y = r
  
  return x
    
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  group = parser.add_mutually_exclusive_group()
  
  parser.add_argument('string', type=str, nargs='*', default=sys.stdin)
  parser.add_argument('-k', '--key', type=int, nargs=2, metavar=('a', 'b'))
  group.add_argument('-d', '--decrypt', action='store_true')
  group.add_argument('-e', '--encrypt', action='store_true')
  
  args = parser.parse_args()
  
  if gcd(args.key[0]) != 1:
    print('key value "a" ({}) must be coprime to 26.'.format(args.key[0]))
    sys.exit()
  
  if not sys.stdin.isatty():
    args.string = args.string.read().replace('\n', '')
  elif isinstance(args.string, list):
    args.string = ' '.join(args.string)
  else:
    print('Need string to work with.')
    sys.exit()
    
  if not args.encrypt and not args.decrypt:
    print('Must choose to encrypt or decrpyt.')
    sys.exit()
    
  action = 'encrypt' if args.encrypt else 'decrypt'
  
  print(getattr(AffineCipher(args.key[0], args.key[1]), action)(args.string))