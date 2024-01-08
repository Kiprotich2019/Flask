from flask import Flask,render_template,request


app1=Flask(__name__)

@app1.route('/')
def Welcome():
    return "Welcome to the Flask"

print(__name__)

@app1.route('/cal', methods='GET')
def math_operator():
    operation=request.json("operation")
    number1=request.json("number1")
    number2=request.json("number2")

    if operation=='add':
        result=number1+number2
    elif operation=='multiplication':
        result=number1*number2
    elif operation=='division':
        result=number1/number2
    else:
        result=number1-number2




if __name__=='__main__':
    app1.run(debug=True)

