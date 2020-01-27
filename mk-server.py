from flask import Flask, request, render_template, redirect
import json
import random

app = Flask(__name__)

# setup
try:
    flags = json.load(open('flags.json'))
except:
    print("No flags file")
    exit(0)


# index
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# task 1
@app.route('/task1', methods=['GET'])
def task1_get():
    return "Just send a <b>POST</b> request..."


@app.route('/task1', methods=['POST'])
def task1_post():
    return flags[0]


# task 2
@app.route('/task2', methods=['GET'])
def task2_get():
    return "Send </b>POST</b> request with your <i>name</i>..."


@app.route('/task2', methods=['POST'])
def task2_post():
    name = request.form.get('name')
    if name:
        return "{}, вот ваш флаг - {}".format(name, flags[1])


# task 3
@app.route('/task3', methods=['GET'])
def task3_get():
    return "Send a </b>LUPA</b> request..."


@app.route('/task3', methods=['LUPA'])
def task3_post():
    return flags[2]


# task 4
@app.route('/task4', methods=['GET'])
def task4_get():
    browser = request.headers.get('User-Agent', None)
    if browser == "LupaBrowser v1.1":
        return flags[3]
    return "This site works only in <i>LupaBrowser v1.1</i>..."


# task 5
@app.route('/task5', methods=['GET'])
def task5_get():
    token = request.args.get('token', None)
    if token == "346":
        return flags[4]
    return "You need to pass <i>token</i> (from 111 to 999) as GET argument..."


# task 6
@app.route('/task6', methods=['GET'])
def task6_get():
    flag = request.args.get('flag', "")
    return render_template("guess.html", flag=flag)


@app.route('/task6', methods=['POST'])
def task6_post():
    number = str(random.randint(1, 40))
    guess = request.form.get('number', '0')

    if guess == number:
        return redirect('/task6?flag=' + flags[5])

    return redirect('/task6?flag=No')


app.run(host='0.0.0.0', port=2020)
