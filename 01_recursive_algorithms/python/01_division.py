def divide(a, b):
  if (b == 0):
    raise Exception("invalid")
  if (a < 0): return -divide(-a, b)
  if (b < 0): return -divide(a, -b)
  if (a < b): return 0
  return 1 + divide(a-b, b);
 
