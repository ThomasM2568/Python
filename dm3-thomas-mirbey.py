#DM n°3 Thomas MIRBEY
def derangement(n):
        if n>=3:
            return((n-1)*(derangement(n-1)+derangement(n-2)))

        if n==2:
            return 1
        if n==1:
            return 0


print(derangement(5))

