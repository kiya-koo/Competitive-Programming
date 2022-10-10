def grading(g):
    for i in range(len(g)):
        if g[i]>=38:
            n1=g[i]//5
            n2=(n1+1)*5-g[i]
            if n2<3:
                g[i]=(n1+1)*5
    return g
