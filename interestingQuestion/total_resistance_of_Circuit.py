import re

circuit = '3 5 S 0 P 3 2 S P'

pattern = re.compile('(\d+) +(\d+) +([SP])')


def parallel_or_serie(m):
  a, b, sp = m.groups()
  if sp == 'S':
    return str(int(a) + int(b))
  else:
    if a == '0' or b == '0':
      return '0'
    else:
      return str(1/(1/int(a) + 1/int(b)))

while True:
  print(circuit)
  tmp = circuit
  circuit = re.sub(pattern, parallel_or_serie, circuit, count=1)
  if tmp == circuit:
    break
