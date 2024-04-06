from flask import Flask, render_template, request

from games.guess_numbers.guessing_numbers import GuessingNumbers
from games.number_baseball_game.numbers_baseball import NumbersBaseball
from games.star_drawing.star_drawer import StarDrawer
from games.star_drawing.utils import get_digit, get_alias

import random
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/star', methods=['GET'])
def start():
    return render_template('star_01.html')   

@app.route('/star_draw', methods=['POST'])
def start_draw():
    alias = request.form['alias']
    num_lines = int(request.form['num_lines'])

    star_drawer = StarDrawer(alias=alias, num_lines=num_lines)
    drawing = star_drawer.draw_stars()

    # star = Star(shape, line_cnt)
    # star.darw_starts(align)     
    # drawing = star.get_drawing(align)     
    # print(drawing)
    return render_template('star_02.html', drawing=drawing)      

@app.route('/guess_number', methods=['GET'])
def guess_number():
    return render_template('guess_number.html')   

@app.route('/guess_number_init', methods=['POST'])
def guess_number_init():
    player = request.form['player']
    random_number = random.randrange(1,100)
    with open(f'guess_number_{player}.txt', 'w') as f:
        f.write(str(random_number) + '\n')
    return render_template('guess_number_init.html', player=player)   

@app.route('/guess_number_proc', methods=['POST'])
def guess_number_proc():
    player = request.form['player']
    guessed_number = int(request.form['guess'])
    with open(f'guess_number_{player}.txt', 'r') as f:
        lines = f.readlines()
        random_number = int(lines[0])
        input_numbers = lines[1:]
    message = ''
    is_right = False
    if random_number > guessed_number:
        message = '정답보다 값이 작습니다.'
    elif random_number < guessed_number:
        message = '정답보다 값이 큽니다.'
    else:
        message = '정답입니다.'
        is_right = True
        # 파일 삭제
        delete_file = f'guess_number_{player}.txt'
        os.remove(delete_file)
    if not is_right:
        with open(f'guess_number_{player}.txt', 'a') as f:
            f.write(str(guessed_number) + '\n')
    return render_template('guess_number_form.html', player=player, guessed_number=guessed_number, message=message, input_numbers=input_numbers, is_right=is_right)        

@app.route('/number_baseball', methods=['GET'])
def number_baseball():
    return '<h1>number_baseball</h1>'          

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5050', debug=True)