# 7번에서 입력한 줄 개수가 숫자가 아닐 경우 숫자를 입력할 때까지 계속 입력 받기

while True:
    num_lines_str = input('별의 줄 수를 입력하세요: ')
    if not num_lines_str.isdigit():
        print('입력하신 값이 숫자가 아닙니다!')
    else:
        break

num_lines = int(num_lines_str)

for i in range(num_lines):
    print((' ' * (num_lines - i)) + '*' * (i*2+1)) 