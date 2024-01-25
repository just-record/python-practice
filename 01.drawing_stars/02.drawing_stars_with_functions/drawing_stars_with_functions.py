# 아래의 소스 코드를 함수를 사용하여 재작성하시오.
# while True:
#     num_lines_str = input('input number of lines: ')
#     if not num_lines_str.isdigit():
#         print('입력하신 값이 숫자가 아닙니다!')
#     else:
#         break

# num_lines = int(num_lines_str)

# for i in range(num_lines):
#     print((' ' * (num_lines - i)) + '*' * (i*2+1)) 


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
    input_message = 'input number of lines: '
    num_lines = get_digit(input_message)
    draw_stars(num_lines)

main()    

