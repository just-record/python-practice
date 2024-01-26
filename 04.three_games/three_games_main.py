from games.guess_numbers.guessing_numbers import GuessingNumbers
from games.number_baseball_game.numbers_baseball import NumbersBaseball
from games.star_drawing.star_drawer import StarDrawer
from games.star_drawing.utils import get_digit, get_alias

def display_start(message):
    print('=========================')
    print()
    print(message)
    print()

if __name__ == '__main__':
    input_message = ' \n' \
                    '=========================\n' \
                    '1: 별 그리기\n' \
                    '2: 숫자 맞추기\n' \
                    '3: 숫자 야구 게임\n' \
                    'q: 종료\n' \
                    '원하시는 번호를 입력하세요: '
    while True:
        menu = input(input_message)
        print(f'선택한 메뉴: {menu}')
        if menu == '1':

            display_start('별 그리기를 시작합니다.')

            input_alias = '별칭을 입력 하세요: '
            alias = get_alias(input_alias)
            input_num_of_lines = '별의 줄 수를 입력하세요: '
            num_lines = get_digit(input_num_of_lines)

            star_drawer = StarDrawer(alias=alias, num_lines=num_lines)
            star_drawer.draw_stars()

        elif menu == '2':

            display_start('숫자 맞추기를 시작합니다.')

            guessing_numbers = GuessingNumbers()
            guessing_numbers.play()
            
        elif menu == '3':

            display_start('숫자 야구 게임을 시작합니다.')

            number_baseball = NumbersBaseball()
            number_baseball.play_game()

        elif menu == 'q':
            break
        else:
            print('잘못 입력하셨습니다. 다시 입력해주세요.')