from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("Home.html")


# Variable Rule
@app.route('/success/<int:score>')
def success(score):
    return "The marks you got is "+ str(score)

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

@app.route('/submit',methods=['POST','GET'])
def get_result():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c =  float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('results',score = total_score))


if __name__ == "__main__":
    app.run(debug=True)
