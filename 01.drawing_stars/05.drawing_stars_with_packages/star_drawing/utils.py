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
