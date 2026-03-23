import sys

alp=""
for i in range(97, 123):
    alp+=chr(i)
dic={}
for i in range(len(alp)):
    dic[alp[i]]=0

input_str=sys.stdin.read()
for s in input_str:
    if s.lower() in alp:
        dic[s.lower()]+=1

for i in range(26):
    print(alp[i],":", dic[alp[i]])