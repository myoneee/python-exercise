#문제 1
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#결과 : shirt 출력


#문제2
i=0
count =0
while i != 101:
    i = i+1
    if i%4 == 0:
        count = count + i
print(count)


#문제3
i=0
count = 0
for i in range(1,100):
    i = i+1
    if i%5 == 0:
        count = count + i
print(count)


#문제4
a = 0
count = 0
py_score = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
for i in range(0,9):
    if py_score[i] > 60:
        a += py_score[i]        
        count = count + 1
print(a/count)


#문제5
for i in range(2,10):
    for j in range(1,10):
        print(i, "*", j, '=', i*j) 


#문제6
sentence = ['다들', '파이썬은', '어떠신가요', '파이썬은', '나중에', '다른', '곳에서도', '많이', '쓰인답니다', '파이썬은','다른','언어보다', '코딩', '하기', '쉬워요', '멋사', '멋사', '화이팅']
word_cnt = dict() 
for word in sentence: 
    if word not in word_cnt.keys(): 
        word_cnt[word] = 1 
    else: 
        word_cnt[word] += 1
print(word_cnt) 

     
