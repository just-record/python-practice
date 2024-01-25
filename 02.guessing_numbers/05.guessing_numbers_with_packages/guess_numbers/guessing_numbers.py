import random

class GuessingNumbers:
    def __init__(self):
        self.random_number = random.randrange(1, 100)
        self.cnt = 0
        self.max_cnt = 10
        self.input_numbers = []

    def get_guess(self):
        while True:
            guess_number_str = input('input guess number: ')
            if not guess_number_str.isdigit():
                print('입력하신 값이 숫자가 아닙니다!')
                continue
            if guess_number_str in self.input_numbers:
                print('이미 입력하신 값입니다!')
                continue
            return guess_number_str

    def check_guess(self, guess_number):
        if self.random_number > guess_number:
            print('입력하신 값이 작습니다!')
        elif self.random_number < guess_number:
            print('입력하신 값이 큽니다!')
        else:
            print('정답입니다.')
            return True
        if self.cnt >= self.max_cnt:
            print(f'{self.max_cnt}번째 시도하셨으나 맞추지 못하였습니다. 탈락입니다.')
            return True
        return False

    def play(self):
        print(self.random_number)  # 게임 테스트용 출력, 실제 게임에서는 제거
        while True:
            guess_number_str = self.get_guess()
            self.input_numbers.append(guess_number_str)
            self.cnt += 1
            print(f'{self.cnt}번째 시도입니다.')
            if self.check_guess(int(guess_number_str)):
                break
