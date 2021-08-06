from flask import Flask, render_template, send_file
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/img/get/<number>')
def sever_img(number):
    file_name = './static/pics/' + number + '.jpg'
    return send_file(file_name)

app.run(host="localhost", port=5000)