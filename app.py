from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sum', methods=['POST'])
def sum():
    try:
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        return render_template('index.html', result=result)
    except ValueError:
        return render_template('index.html', result="Por favor, ingrese números válidos.")

if __name__ == '__main__':
    app.run(debug=True)
