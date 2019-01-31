import random ,sys
cate=['game','fruit']
print('Select Category: ')
print()
print('1 Game')
print('2 Fruit')
print()
n=int(input('Type: 1 or 2  '))



file = open(cate[n-1]+'.txt','r')
dic={}
for i in file:
    dic[(i.split('/'))[0]]=(i.split('/'))[1].strip('\n')
word,hint = random.choice(list(dic.items()))
score=0
rem=5

res=['_' for x in range(len(word))]
print()
print('###############################')
print()
print('Hint: ',hint)
print()
print(*res,'      ','score: ',score,'  remaining wrong guess',rem)
print()
while(True):
    if ("".join(res))==word:
        print("Congratulation!!! You win")
        print()
        print('score: ',score)
        break
    else:
        guess=input('Enter alphabet: ')
        print()
        if (guess.lower() in word.lower()) and (guess.lower() not in ("".join(res)).lower()):
            for i in range(len(word)):
                if word[i].lower()==guess.lower():
                    res[i]=word[i]
                    score+=10
            print(*res,'      ','score: ',score,'  remaining wrong guess',rem,)
            print()
        else:
            rem-=1
            print(*res,'      ','score: ',score,'  remaining wrong guess',rem,'  wrong guessed: ',guess)
            print()
            if rem==0:
                print(*res,'      ','score: ',score,'  remaining wrong guess',rem,'  wrong guessed: ',guess)
                print('You lose , better try harder')
                print()
                print('Answer: ',word)
                print()
                break
sys.exit()                
