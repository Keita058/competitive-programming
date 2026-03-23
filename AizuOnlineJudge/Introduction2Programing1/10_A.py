x1,y1,x2,y2=map(float, input().split())
dist=((x1-x2)**2+(y1-y2)**2)**0.5
print(round(dist,5))