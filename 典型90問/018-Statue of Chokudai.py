from math import sqrt,atan,pi,sin,cos

def cal_pos(t):
    res_y=-L/2*sin(t/T*(2*pi))
    res_z=L/2*(1-cos(t/T*(2*pi)))
    return res_y,res_z

def cal_theta(p,q):
    TAN=q/sqrt(X**2+(Y-p)**2)
    res=atan(TAN)*180/pi
    return res

T=int(input())
L,X,Y=map(int,input().split())
Q=int(input())
for _ in range(Q):
    e=int(input())
    p,q=cal_pos(e)
    ans=cal_theta(p,q)
    print(ans)