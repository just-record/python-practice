# 중복 되지 않는 임의의 3자리 숫자를 생성하기

import random

random_numbers = ''

while True:
    temp_random_number = str(random.randrange(0, 10))
    
    if temp_random_number not in random_numbers:
        random_numbers += temp_random_number
    if len(random_numbers) == 3:
        break

print(random_numbers)