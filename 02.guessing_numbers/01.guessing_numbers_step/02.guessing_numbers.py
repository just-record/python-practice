# 사용자로 부터 추측값을 입력 받고 숫자가 아닌 경우 계속 입력 받기. 이 때 정답과 추측값을 출력하기

import random

random_number = random.randrange(1,100)

while True:
    guess_number_str = input('input guess number: ')
    if not guess_number_str.isdigit():
        print('입력하신 값이 숫자가 아닙니다!')
        continue
    
    guess_number = int(guess_number_str)   
    print(random_number, guess_number)
    break
