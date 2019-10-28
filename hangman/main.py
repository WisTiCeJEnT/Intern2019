import random, sys, os
cate = ['game', 'fruit']
WELCOME_TEXT = """
Select Category: 

1 Game
2 Fruit

"""
print(WELCOME_TEXT)
n = int(input('Type: 1 or 2  '))

file = open(cate[n-1]+'.txt','r')
dic={}
for i in file:
    dic[(i.split('/'))[0]] = (i.split('/'))[1].strip('\n')
word, hint = random.choice(list(dic.items()))
score = 0
rem = 5
guessed = ""

res = ['_' for x in range(len(word))]
HINT_TEXT = f"""
###############################')

Hint: {hint}

"""
while(True):
    os.system('clear')
    print(HINT_TEXT)
    print(*res,'      ','score: ',score,'  remaining wrong guess',rem,  f"wrong guessed: {guessed}" if guessed != "" else "", end = '\n\n')
    if ("".join(res)) == word:
        WIN_TEXT = f"""
        Congratulation!!! You win

        score: {score}
        """
        print(WIN_TEXT)
        break
    else:
        guess = input('Enter alphabet: ')
        guessed += f"{guess} "
        if (guess.lower() in word.lower()) and (guess.lower() not in ("".join(res)).lower()):
            for i in range(len(word)):
                if word[i].lower() == guess.lower():
                    res[i] = word[i]
                    score += 10
        else:
            rem -= 1
            if rem == 0:
                LOSE_TEXT = f"""
                You lose , better try harder

                Answer: {word}
                """
                print(LOSE_TEXT)
                break
sys.exit()                
