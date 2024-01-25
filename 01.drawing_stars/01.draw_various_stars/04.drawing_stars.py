# 첫째 줄에 별 1개 그리고 줄이 바뀌면 별을 1개씩 늘려가면서 5줄 그릴 때 별이 오른쪽으로 정렬되게 그리기

num_lines = 5

for i in range(1, num_lines + 1):
    print(' ' * (num_lines - i) + '*' * i)    