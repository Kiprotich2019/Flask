from flask import Flask,request
#import json

app1=Flask(__name__)

@app1.route('/')
def Welcome():
    return "Welcome to the Flask"

print(__name__)

@app1.route('/cal', methods=['GET'])
def math_operator():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    if operation=='add':
        result=int(number1)+int(number2)
    elif operation=='multiplication':
        result=int(number1)*int(number2)
    elif operation=='division':
        result=int(number1)/int(number2)
    else:
        result=int(number1)-int(number2)
    
    return "The operation is {} and the result is {}".format(operation,result)


if __name__=='__main__':
    app1.run(debug=True)

