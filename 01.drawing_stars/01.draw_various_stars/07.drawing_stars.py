# 6번에서 줄 개수에 숫자가 아닌 문자를 넣었을 때 처리하기

num_lines_str = input('input number of lines: ')
if num_lines_str.isdigit():
    num_lines = int(num_lines_str)

    for i in range(num_lines):
        print((' ' * (num_lines - i)) + '*' * (i*2+1))          
else:
    print('입력하신 값이 숫자가 아닙니다!')