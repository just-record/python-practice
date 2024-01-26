# python_practice

파이썬의 기본 문법을 익힌 후 연습하기

## 별 그리기

피라미드 모양의 별을 출력하는 프로그램

### 01.drawing_stars

| 설명 | 하위 디렉토리 |
|:---:|:---:|
| 여러가지 별 그리기 | 01.draw_stars_step |
| 함수를 써서 별 그리기 | 02.drawing_stars_with_functions |
| 클래스를 써서 별 그리기 | 03.drawing_stars_with_classes |
| 모듈을 써서 별 그리기 | 04.drawing_stars_with_modules |
| 패키지를 써서 별 그리기 | 05.drawing_stars_with_packages |

## 숫자 맞추기 게임

프로그램이 생각한 숫자를 맞추는 프로그램

### 02.guessing_numbers

프로그램이 생각한 숫자를 추측합니다. 정답과 비교하면 작은지 큰지 알려줍니다.

<!-- | 설명 | 소스 디렉토리 |
|:---:|:---:|
| 숫자 맞추기 | 01.guessing_numbers | -->

## 숫자 야구 게임

아주 유명한 숫자 야구 게임

### 03.number_baseball

[숫자 야구 게임 규칙](https://namu.wiki/w/%EC%88%AB%EC%9E%90%EC%95%BC%EA%B5%AC)

## 위의 3가지 게임을 모두 포함한 게임

별 그리기, 숫자 맞추기, 숫자 야구 게임을 모두 포함한 게임

### 04.three_games

3가지 게임을 패키지로 만들고 3가지 중 하나를 선택하면 해당 게임을 실행 하도록 구현

## 위의 3가지 게임을 웹 서비스로 만들기(작업중)

바로 위에서 만든 3가지 게임의 패키지를 그대로 사용하여 웹 서비스로 만들기

- 해당 실습 프론트엔드(HTML, CSS, JavaScript)와 백엔드(Flask)의 사전 학습이 필요합니다.

### 05.three_games_web

Flask를 사용하여 3가지 게임을 웹 서비스로 만들기

### requirements.txt

웹 서비스를 만들기 위해서는 requirements.txt에 있는 패키지를 설치해야 합니다.

```bash
pip install -r requirements.txt
```

pip 업그레이드가 필요할 수 있습니다.

```bash
python.exe -m pip install --upgrade pip
```