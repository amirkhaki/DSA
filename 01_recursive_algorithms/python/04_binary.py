def _binary(a):
    if a == 0: return
    _binary(a//2)
    print(a%2, end='')

def binary(a):
    _binary(a)
    print()
