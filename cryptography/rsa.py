# coding: utf-8

import sys, argparse
  
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

def generate_key_pair(p: int, q: int, e: int) -> tuple:
  n = p * q
  phi = (p - 1) * (q - 1)  
  d = inverse(e, phi)
  
  return ((n, e), (n, d))

def gcd(a: int, b: int) -> int:
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

def inverse(a, n):
  '''
  Extended Euclidean algorithm adaptation
  Credit: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
  '''
  t, new_t = 0, 1
  r, new_r = n, a
  
  while new_r != 0:
    quotient = r // new_r
    t, new_t = new_t, t - quotient * new_t
    r, new_r = new_r, r - quotient * new_r
    
  if r > 1:
    raise ValueError('a ({}) is not invertible'.format(a))
  if t < 0:
    t = t + n
    
  return t

def is_prime(n: int) -> bool:
    '''
    Simple primality test
    Credit: https://en.wikipedia.org/wiki/Primality_test
    '''
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
      
    limit = int(n ** 0.5)
    
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  group = parser.add_mutually_exclusive_group()
  
  parser.add_argument('string', type=str, nargs='+')
  parser.add_argument('-p', '--primes', type=int, nargs=2, metavar=('p', 'q'), required=True)
  parser.add_argument('-ex', '--exponent', type=int, required=True)
  group.add_argument('-d', '--decrypt', action='store_true')
  group.add_argument('-e', '--encrypt', action='store_true')

  args = parser.parse_args()
  
  if not args.encrypt and not args.decrypt:
    print('Must choose to encrypt or decrpyt.')
    sys.exit()
  
  if not (is_prime(args.primes[0]) and is_prime(args.primes[1])):
    print('both primes p and q must be prime.')
    sys.exit()
  
  if args.primes[0] == args.primes[1]:
    print('primes p and q must be different.')
    sys.exit()
    
  if gcd(args.exponent, (args.primes[0] - 1) * (args.primes[1] - 1)) != 1:
    print('exponent and totient function must be coprime.')
    sys.exit()
    
  args.string = ' '.join(args.string)

  public, private = generate_key_pair(args.primes[0], args.primes[1], args.exponent)
  
  if args.encrypt:
    t = [CHAR_TO_NUM[c.upper()] for c in list(args.string)]
    t = [int(str(c[0]) + str(c[1])) for c in zip(t[0::2], t[1::2])]
    t = [pow(c, public[1], public[0]) for c in t]
    print(t)
  else:
    t = [int(c) for c in args.string.split(' ')]
    t = [str(pow(c, private[1], private[0])).zfill(4) for c in t]
    t = [NUM_TO_CHAR[int(c[:2])] + NUM_TO_CHAR[int(c[2:])] for c in t]
    print(t)