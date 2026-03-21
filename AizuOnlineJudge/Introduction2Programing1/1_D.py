S=int(input())
hh=S//3600
S=S-hh*3600
mm=S//60
S=S-mm*60
ss=S
ans=str(hh)+":"+str(mm)+":"+str(ss)
print(ans)