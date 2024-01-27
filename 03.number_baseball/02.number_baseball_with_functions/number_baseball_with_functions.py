import random

def generate_random_number():
    random_numbers = ''
    while len(random_numbers) < 3:
        temp_random_number = str(random.randrange(0, 10))
        if temp_random_number not in random_numbers:
            random_numbers += temp_random_number
    return random_numbers

def get_user_input(input_numbers):
    while True:
        guess_numbers = input('Input guess number: ')
        if not guess_numbers.isdigit() or len(guess_numbers) != 3:
            print('입력하신 값이 3자리 숫자가 아닙니다!')
        elif len(set(guess_numbers)) != len(guess_numbers):
            print('중복된 값을 입력하셨습니다.')
        elif guess_numbers in input_numbers:
            print('이전에 입력한 값입니다.')
        else:
            return guess_numbers

def analyze_guess(guess_numbers, random_numbers):
    strike, ball = 0, 0
    for i in range(3):
        if guess_numbers[i] == random_numbers[i]:
            strike += 1
        elif guess_numbers[i] in random_numbers:
            ball += 1
    return strike, ball

def play_game():
    random_numbers = generate_random_number()
    # print(random_numbers)

    input_numbers = []

    max_cnt = 10
    for total_cnt in range(1, max_cnt + 1):
        guess_numbers = get_user_input(input_numbers)
        input_numbers.append(guess_numbers)
        print(f'{total_cnt}번째 시도입니다.')
        strike, ball = analyze_guess(guess_numbers, random_numbers)
        print(f'{strike} Strike, {ball} Ball, {3 - (strike + ball)} Out')

        if strike == 3:
            print(f'{total_cnt}번째 성공했습니다!')
            return
        elif total_cnt == max_cnt:
            print(f'{max_cnt}을 시도하셨지만 실패하였습니다. 게임을 종료합니다.')
            return

# Start the game
play_game()