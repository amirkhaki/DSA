def truth_table(n, prefix = ""):
    if n == 0:
        print(prefix)
        return
    
    truth_table(n-1, f'{prefix} 0')
    truth_table(n-1, f'{prefix} 1')
