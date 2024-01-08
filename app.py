from flask import Flask,render_template,request,url_for,redirect
app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, world!</h1>"


@app.route('/Welcome')
def Welcome():
    return "Welcome to Flask tutorials"


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    return 'The student has passed and the score is '+str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return 'The student has failed and the score is '+str(score)


@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        stats=float(request.form['stats'])
        econ=float(request.form['econ'])
        maths=float(request.form['maths'])

        Average_marks=(stats+econ+maths)/3
        result=""
        if Average_marks>=50:
            result="success"
        else:
            result="fail"
        #return redirect(url_for(result,score=Average_marks))
        return render_template('result.html',results=Average_marks)
    









if __name__=='__main__':
    app.run(debug=True)