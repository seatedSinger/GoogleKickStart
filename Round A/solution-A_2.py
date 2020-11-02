inp =int(input())
A=[]
for t in range(1,inp+1):
    N,B=[int(s) for s in input().split(" ")]
    A=list(map(int, input().split()))
    count=0
    A.sort()
    for i in range(len(A)):
        if(B>=A[i]):
            B=B-A[i]
            count+=1
    #* F string print
    A.clear()