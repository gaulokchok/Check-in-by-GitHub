def polynomial(coef):
    def p(x):
        for i in range(len(coef)):
            result += coef[i]*(x**(len(coef)-1-i))
        return result
    return p
def invert(y,p):
    a = 0
    b = y
    while p((a+b)//2)!= y:
        if p((a+b)//2) > y:
            b = (a+b)//2
        elif p((a+b)//2) < y:
            a = (a+b)//2
    return (a+b)//2