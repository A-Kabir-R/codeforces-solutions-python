def solve():
    x,y,a,b=map(int,input().split())
    value=b-a-y+x
    if b<y or value<0 :
        print(-1)
        #print("\n")
        return
    else :
        c=y-x
        xx=b-c
        yy=b
        step=abs(xx-a)
        step+=abs(x-xx)
        print(step)
        #print("\n")
        return

t=int(input())

for i in range(t):
    solve()