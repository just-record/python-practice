# 10번 시도해서 정답을 맞추지 못하면 탈락시키기

import random

random_number = random.randrange(1,100)
# print(random_number) # for debugging

cnt = 0
max_cnt = 10

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
    
    if cnt >= max_cnt:
        print(f'{max_cnt}번째 시도하셨으나 맞추지 못하였습니다. 탈락입니다.')
        break    