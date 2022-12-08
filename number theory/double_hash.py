# coding: utf-8

import argparse

def h(k: int, p: int) -> int:
  return k % p

def g(k: int, p: int) -> int:
  return (k + 1) % (p - 2)

def probe(k: int, i: int, p: int) -> int:
  return (h(k, p) + i * g(k, p)) % p

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument('-p', '--prime', type=int, help='prime modulus')
  parser.add_argument('-n', '--numbers', type=int, metavar='NUMBER', nargs='+', help='numbers to hash')

  args = parser.parse_args()
  
  h_values = {}
  probes = {}
  
  print('\nInitial hashes:')
  for i, k in enumerate(args.numbers, 1):
    h_result = h(k, args.prime)
    
    print('h({number}) = {number} mod {prime} = {result}'
          .format(number=k, prime=args.prime, result=h_result))
    
    if h_result in h_values.keys():
      h_values[h_result].append((k, i))
    else:
      h_values[h_result] = [(k, i)]

  print('\nCollisions:')
  for key, val in h_values.items():
    if len(val) > 1:
      print('{}:'.format(key), end=' ')
      
      for _h in val:
        print(_h[0], end=' ')
        probes[probe(_h[0], _h[1], args.prime)] = _h
      
      print()
  
  print('\nProbing sequences:')
  for key, val in probes.items():
    print('h({k}, {i}) = (h({k} + {i} * g({k})) mod {p} = {r}'
          .format(k=val[0], i=val[1], p=args.prime, r=key))