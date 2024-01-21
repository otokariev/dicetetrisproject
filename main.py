from flask import Flask, render_template

app = Flask(__name__)

# Ваша матрица с буквами
matrix = [
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
    ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'a'],
    ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'a'],
    ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'a'],
    ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'a'],
    ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'a'],
    ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'a'],
    ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'a'],
    ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'a'],
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
]

# Пути к изображениям
image1_path = 'static/black.jpg'
image2_path = 'static/white.jpg'

# Заменяем буквы в матрице на пути к изображениям
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'a':
            matrix[i][j] = image1_path
        elif matrix[i][j] == 'b':
            matrix[i][j] = image2_path


@app.route('/')
def index():
    return render_template('index.html', matrix=matrix)


if __name__ == '__main__':
    app.run(debug=True)
