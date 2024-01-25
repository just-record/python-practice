# 숫자 야구 게임 완성하기

import random

random_numbers = ''

while True:
    temp_random_number = str(random.randrange(0, 10))
    
    if temp_random_number not in random_numbers:
        random_numbers += temp_random_number
    if len(random_numbers) == 3:
        break

print(random_numbers)

total_cnt, max_cnt = 0, 10


while True:

    strike, ball = 0, 0
    # out은 3 - (strike + ball)로 계산

    guess_numbers = input('input guess number: ')   
    # 3자리 숫자인지 체크
    if not guess_numbers.isdigit() or len(guess_numbers) != 3:
        print('입력하신 값이 3자리 숫자가 아닙니다!')
        continue

    # 중복값이 있는지 체크
    if len(set(guess_numbers)) != len(guess_numbers):
        print('중복된 값을 입력하셨습니다.')
        continue

    print(f'입력하신 값은 {guess_numbers}입니다.')

    total_cnt += 1
    print(f'{total_cnt}번째 시도입니다.')

    # 결과 분석하기
    for i in range(len(guess_numbers)):
        if guess_numbers[i] == random_numbers[i]:
            strike += 1
        elif guess_numbers[i] in random_numbers:
            ball += 1

    print(f'{strike}: Strike, {ball}: Ball, {3 - (strike + ball)}: Out')
    
    # 모두 맞추었으면 성공 메세지와 게임 종료
    if strike == 3:
        print(f'{total_cnt}번째 성공했습니다!')
        break

    if total_cnt >= max_cnt:
        print(f'{max_cnt}을 시도하셨지만 실패하였습니다. 게임을 종료합니다.')
        break    