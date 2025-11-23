def solve():
    n=int(input())
    s=input().strip()

    v=[]
    ct=0

    for c in s:
        if c=='.':
            ct+=1
        else: 
            v.append(ct)
            ct=0

    if ct!=0:
        v.append(ct)

    v.sort(reverse=True)
    if(v[0]>=3):
        print(2)
    else: 
        print(sum(v))
    return
    

t = int(input())

for i in range(t):
    solve()
