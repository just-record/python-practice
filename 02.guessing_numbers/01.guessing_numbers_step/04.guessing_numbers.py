# 몇 번 만에 정답을 맞췄는지 표시해주기

import random

random_number = random.randrange(1,100)
# print(random_number)

cnt = 0

while True:
    guess_number_str = input('input guess number: ')
    if not guess_number_str.isdigit():
        print('입력하신 값이 숫자가 아닙니다!')
        continue

    cnt += 1
    print(f'{cnt}번째 시도입니다.')
    guess_number_str = int(guess_number_str)    

    if random_number > guess_number_str:
        print('입력하신 값이 작습니다!')
    elif random_number < guess_number_str:
        print('입력하신 값이 큽니다!')
    else:
        print('정답입니다.')    
        break
    