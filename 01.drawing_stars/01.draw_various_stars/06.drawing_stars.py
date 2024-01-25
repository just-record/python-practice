# 별을 그릴 줄의 개수를 입력 받아서 그리기

num_lines = int(input('input number of lines: '))

for i in range(num_lines):
    print((' ' * (num_lines - i)) + '*' * (i*2+1))  