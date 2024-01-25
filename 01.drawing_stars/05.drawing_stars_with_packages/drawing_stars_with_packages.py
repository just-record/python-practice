from star_drawing.star_drawer import StarDrawer
from star_drawing.utils import get_digit, get_alias

def main():
    input_message = '별칭을 입력 하세요: '
    alias = get_alias(input_message)
    input_message = '별의 줄 수를 입력하세요: '
    num_lines = get_digit(input_message)

    star_drawer = StarDrawer(alias=alias, num_lines=num_lines)
    star_drawer.draw_stars()

if __name__ == "__main__":
    main()
