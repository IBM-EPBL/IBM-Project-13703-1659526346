from flask import Flask, render_template, redirect, request, url_for, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addcategory')
def addcategory():
    return render_template('addcategory.html')

@app.route('/expensestatus')
def expensestatus():
    return render_template('expensestatus.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)