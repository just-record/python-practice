def get_digit(input_message):
    while True:
        input_str = input(input_message)
        if input_str.isdigit():
            return int(input_str)
        else:
            print('입력하신 값이 숫자가 아닙니다!')

def draw_stars(num_lines):
    for i in range(num_lines):
        print((' ' * (num_lines - i)) + '*' * (i*2+1))

def main():
    input_message = '별의 줄 수를 입력하세요: '
    num_lines = get_digit(input_message)
    draw_stars(num_lines)

main()    

