# 첫째 줄에 별을 5개 그리고 줄이 바뀌면 별을 1개씩 줄어가면서 5줄 그리기

num_lines = 5

for i in range(num_lines, 0, -1):
    print('*' * i)