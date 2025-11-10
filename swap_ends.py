def swap_ends(L, k):
    #use suffix and preffi
    if k <= 0 or k > len(L) // 2:
        copy_L = L[:]
        return (copy_L, 0)
    
    c = L[:k]
    b = L[k:len(L) - k]
    a = L[-k:]

    return (a + b + c, k)
    
