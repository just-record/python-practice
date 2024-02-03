# 파일에 별 그리기를 저장하기

while True:
    num_lines_str = input('별의 줄 수를 입력하세요: ')
    if not num_lines_str.isdigit():
        print('입력하신 값이 숫자가 아닙니다!')
    else:
        break

num_lines = int(num_lines_str)

with open("start.txt", "w") as f:
    for i in range(num_lines):
        f.write((' ' * (num_lines - i - 1)) + '*' * (i*2+1) + '\n')