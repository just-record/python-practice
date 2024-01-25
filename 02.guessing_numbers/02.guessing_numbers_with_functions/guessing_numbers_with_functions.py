import random

def get_guess(input_numbers):
    while True:
        guess_number_str = input('input guess number: ')
        if not guess_number_str.isdigit():
            print('입력하신 값이 숫자가 아닙니다!')
            continue
        if guess_number_str in input_numbers:
            print('이미 입력하신 값입니다!')
            continue
        return guess_number_str

def check_guess(random_number, guess_number, cnt, max_cnt):
    if random_number > guess_number:
        print('입력하신 값이 작습니다!')
    elif random_number < guess_number:
        print('입력하신 값이 큽니다!')
    else:
        print('정답입니다.')
        return True
    if cnt >= max_cnt:
        print(f'{max_cnt}번째 시도하셨으나 맞추지 못하였습니다. 탈락입니다.')
        return True
    return False

def main():
    random_number = random.randrange(1, 100)
    # print(random_number) # for debugging

    cnt = 0
    max_cnt = 10
    input_numbers = []

    while True:
        guess_number_str = get_guess(input_numbers)
        input_numbers.append(guess_number_str)
        cnt += 1
        print(f'{cnt}번째 시도입니다.')

        if check_guess(random_number, int(guess_number_str), cnt, max_cnt):
            break

if __name__ == "__main__":
    main()
