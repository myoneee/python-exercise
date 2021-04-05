#문제1
def is_odd(num):
    if num % 2 == 0:
        print('짝수')
    else:
        print('홀수')
      
num=int(input())
is_odd(num)


#문제2
num_list = [1, 5, 10, 15, 20]

def average(nums_list):
    avg = 0.0
    for i in nums_list:
         avg += i
    return avg / len(num_list)

