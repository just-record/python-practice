class StarDrawer:
    def __init__(self, alias='StarDrawer', num_lines=5):
        self.alias = alias
        self.num_lines = num_lines

    def draw_stars(self):
        print(f'{self.alias}이(가) 그립니다.')
        for i in range(self.num_lines):
            print((' ' * (self.num_lines - i - 1)) + '*' * (i * 2 + 1))


def get_digit(input_message):
    while True:
        input_str = input(input_message)
        if input_str.isdigit():
            return int(input_str)
        else:
            print('입력하신 값이 숫자가 아닙니다!')


def get_alias(input_message):
    while True:
        input_str = input(input_message)
        str_len = len(input_str)
        if str_len == 0 or str_len > 10:
            print('별칭을 1자 이상 10자 이하로 입력해주세요!')
        else:
            return input_str


def main():
    input_message = '별칭을 입력 하세요: '
    alias = get_alias(input_message)
    input_message = '별의 줄 수를 입력하세요: '
    num_lines = get_digit(input_message)

    star_drawer = StarDrawer(alias=alias, num_lines=num_lines)
    star_drawer.draw_stars()

main()
