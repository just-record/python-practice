# 첫째 줄에 별 1개 그리고 줄이 바뀌면 별을 2개씩 늘려가면서 5줄 그리기

num_lines = 5

for i in range(num_lines):
    print('*' * (i*2+1))