from flask import Flask, redirect, render_template, request, url_for

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

# Variable Rule
@app.route('/success/<int:score>')
def success(score):
    return "The marks you got is "+ str(score)

# Building url dynamically
@app.route('/result/<int:score>')
def result(score):
    res = ""
    if score >= 50:
        res = 'Passed'
    else:
        res = 'Failed'

    return render_template('result.html',results=res)

@app.route('/results/<int:score>')
def results(score):
    res = ""
    if score >= 50:
        res = 'Passed'
    else:
        res = 'Failed'

    exp = {'score':score,'res':res}

    return render_template('results.html',results=exp)

@app.route('/successif/<int:score>')
def successif(score):

    return render_template('result.html', results=score)

@app.route("/fail/<int:score>")
def fail(score):

    return render_template('result.html', results=score)




if __name__ == "__main__":
    app.run(debug=True)
