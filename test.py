import re

phrase="c'est la dislexie et distopie la distopie et le diaporama"
phrase=phrase.split()
result=[]
for i in range(len(phrase)):
    x = re.search('di', phrase[i])
    if(x!=None):
        result.append(phrase[i][2:])
    else:
    	False
print(result)
str=''
for i in range(len(result)):
    if i==0:
        str=str+result[i]
    elif i==len(result)-1:
        str=str+' et '+result[i]
    else:
        str=str+", "+result[i]
print(str)
