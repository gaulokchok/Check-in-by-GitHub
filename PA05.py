def rechnen(a,b):
    g = []
    for i in range (len(a)):
        g.append(a[i]+b[i])
        return min(g)
def mul(A,B):
    a = A.split(',')
    b = B.split(',')
    c =[]
    d =[]
    f =[]
    h =[]
    k =[]
    for i in a:
        c.append(i.split())
    print (c)
    # c in Integer
    for i in range(len(c)):
        for j in range(len(c[0])):
            c[i][j]=int(c[i][j])
    print (c)
    for i in range (len(b)):
        d.append(b[i].split())
    print (d)
    for i in range (len(d[0])):
        f1=[]
        for j in range (len(d)):
            f1.append(d[j][i])
        f.append(f1)
    print (f)
    #f in Integer
    for i in range(len(f)):
        for j in range(len(f[0])):
            f[i][j]=int(f[i][j])
    print(f)
    for i in range (len(c)):
        h1=[]
        for j in range (len(f)):
            h1.append(rechnen(c[i],f[j]))
        h.append(h1)
    print (h)
    for i in range(len(h)):
        for j in range(len(h[0])):
            h[i][j]=str(h[i][j])
    for i in range (len(h)):
        k.append(' '.join(h[i]))
    return ','.join(k)
def pow (A,n):
    if n == 1:
        l = A
    else:
        l = A
        for i in range (2,(n+1)):
            l = mul(l,A)
    return l
