def i(l):
    if len(l)==0:
        return []
    return [l[-1]]+i(l[:-1])
w=[1,2,3,4,5,6]
print(i(w))