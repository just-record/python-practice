# 사용자로부터 입력 받은 숫자가 3자리 숫자인지 그리고 중복되는 숫자가 있는지 검사하기

import random


while True:
    guess_numbers = input('input guess number: ')   
    # 3자리 숫자인지 체크
    if not guess_numbers.isdigit() or len(guess_numbers) != 3:
        # flag_three_digit = False
        print('입력하신 값이 3자리 숫자가 아닙니다!')
        continue

    # 중복값이 있는지 체크
    if len(set(guess_numbers)) != len(guess_numbers):
        print('중복된 값을 입력하셨습니다.')
        continue
    break

print(f'입력하신 값은 {guess_numbers}입니다.')