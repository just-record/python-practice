class StarDrawer:
    def __init__(self, alias='StarDrawer', num_lines=5):
        self.alias = alias
        self.num_lines = num_lines

    def draw_stars(self):
        print(f'{self.alias}이(가) 그립니다.')
        for i in range(self.num_lines):
            print((' ' * (self.num_lines - i - 1)) + '*' * (i * 2 + 1))