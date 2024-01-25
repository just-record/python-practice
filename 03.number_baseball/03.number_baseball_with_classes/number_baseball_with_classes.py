import random

class NumbersBaseball:
    def __init__(self, max_attempts=10):
        self.random_numbers = self.generate_random_number()
        self.max_attempts = max_attempts

    def generate_random_number(self):
        random_numbers = ''
        while len(random_numbers) < 3:
            temp_random_number = str(random.randrange(0, 10))
            if temp_random_number not in random_numbers:
                random_numbers += temp_random_number
        return random_numbers

    def get_user_input(self):
        while True:
            guess_numbers = input('Input guess number: ')
            if not guess_numbers.isdigit() or len(guess_numbers) != 3:
                print('입력하신 값이 3자리 숫자가 아닙니다!')
            elif len(set(guess_numbers)) != len(guess_numbers):
                print('중복된 값을 입력하셨습니다.')
            else:
                return guess_numbers

    def analyze_guess(self, guess_numbers):
        strike, ball = 0, 0
        for i in range(3):
            if guess_numbers[i] == self.random_numbers[i]:
                strike += 1
            elif guess_numbers[i] in self.random_numbers:
                ball += 1
        return strike, ball

    def play_game(self):
        # print(self.random_numbers)

        for total_cnt in range(1, self.max_attempts + 1):
            guess_numbers = self.get_user_input()
            print(f'{total_cnt}번째 시도입니다.')
            strike, ball = self.analyze_guess(guess_numbers)
            print(f'{strike} Strike, {ball} Ball, {3 - (strike + ball)} Out')

            if strike == 3:
                print(f'{total_cnt}번째 성공했습니다!')
                return
            elif total_cnt == self.max_attempts:
                print(f'{self.max_attempts}을 시도하셨지만 실패하였습니다. 게임을 종료합니다.')
                return

# Start the game
game = NumbersBaseball()
game.play_game()
