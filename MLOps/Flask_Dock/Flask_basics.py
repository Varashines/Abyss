from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("Home.html")

@app.route("/teju",methods=['GET'])
def teju():
    return "I Love You"

@app.route("/index",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('index.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
