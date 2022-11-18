from flask import Flask, render_template, redirect, request, url_for, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addincome')
def addIncome():
    return render_template('addincome.html')
@app.route('/showincome')
def showincome():
    return render_template('showincome.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)