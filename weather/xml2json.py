def extract(s):
    InTag=s[s.find('<'):s.find('>')+1].strip('</>').split('"')[:-1]
    OutTag=s[1:][s[1:].find('>')+1:s[1:].find('<')]
    FirstTag=s[s.find('<'):s.find('>')+1].strip('</>').split('"')[0].split()
    res=[]
    dic={}
    for i in range(0,len(InTag),2):
        if i==0:
            res.append(InTag[0].split()[0])
            dic[InTag[0].strip().split()[1].strip('=')]=InTag[1]
        else:
            dic[InTag[i].strip(' =')]=InTag[i+1]
    if len(OutTag)!=0:
        if len(FirstTag)==1:
            res.append(FirstTag[0])
            res.append(OutTag.strip())
        else:
            dic['#TEXT']=OutTag.strip()
    elif len(FirstTag)==1:
        res.append(FirstTag[0])
    if len(dic)!=0:
        res.append(dic)
    return res
   


line=open('read.xml','r')
text=''
for i in line:
    text+=i.strip()
stack=[]
tmp=text[0]
for i in range(1,len(text)-1):
    tmp+=text[i]
    if text[i]=='>' and text[i+1]=='<':
        stack.append(tmp)
        tmp=''
    if i==len(text)-2:
        tmp+=text[len(text)-1]
        stack.append(tmp)

stack=stack[1:len(stack)-1]
sep=[]
tmp=[]
i=0
while i<len(stack):
    s=stack[i]
    
    t=s[s.find('<')+1:s.find(' ')+1]
    
    if (t ==''):
        
        end=stack.index('<'+'/'+s.strip('<>')+'>')
        sep.append(stack[i:end+1])
        i=end+1
        continue
    if (('<'+'/'+t.strip()+'>') in stack):
        end=stack.index('<'+'/'+t.strip()+'>') 
        sep.append(stack[i:end+1])
        i=end+1
        continue
    else:
        sep.append([stack[i]])
        i+=1
    
for i in sep:
    print(i)
res={}
for i in range(len(sep)):
    get=extract(sep[i][0])
    if len(get)!=1:
        k=get[0]
        v=get[1]
        n=len(sep[i])
        for j in range(len(sep[i])-2):
            inget=extract(((sep[i])[1:n-1])[j])
            ink=inget[0]
            inv=inget[1]
            v[ink]=inv
        res[k]=v
    else:
        k=get[0]
        v={}
        n=len(sep[i])
        for j in range(len(sep[i])-2):
            inget=extract(((sep[i])[1:n-1])[j])
            ink=inget[0]
            inv=inget[1]
            v[ink]=inv
        res[k]=v

    


