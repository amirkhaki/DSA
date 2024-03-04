def multiply(a, b):
    if a == 0 or b == 0: return 0
    if a < 0: return -multiply(-a, b)
    if b < 0: return -multiply(a, -b)
    return b + multiply(a-1, b)
