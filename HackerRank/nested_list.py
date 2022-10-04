
if __name__ == '__main__':
    Result =[]
    scorelist = []
    for i in range(int(input())):
        stuname = input()
        stuscore = float(input())
        Result+=[[stuname,stuscore]]
        scorelist+=[stuscore]
    z=sorted(list(set(scorelist)))[1] 
    for x,y in sorted(Result):
        if y==z:
            print(x)
