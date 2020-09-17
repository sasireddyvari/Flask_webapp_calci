from flask import Flask, render_template, request, jsonify

app_calc = Flask(__name__)


@app_calc.route('/', methods=['GET', 'POST'])  # To render Homepage
def home_page():
    return render_template('index.html')


@app_calc.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if request.method == 'POST':
        try:
            operation = request.form['operation']
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            if operation == 'add':
                r = num1 + num2
                result = 'The sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            elif operation == 'subtract':
                r = num1 - num2
                result = 'The difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            elif operation == 'multiply':
                r = num1 * num2
                result = 'The product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            elif operation == 'divide':
                r = num1 / num2
                result = 'The quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
            else:
                result = 'Please specify valid operation'
            return render_template('results.html', result=result)
        except Exception as e:
            result = "An Exception "+str(e)+" Occurred"
            return render_template('results.html', result=result)


@app_calc.route('/via_postman', methods=['POST'])  # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if request.method == 'POST':
        try:
            operation = request.json['operation']
            num1 = int(request.json['num1'])
            num2 = int(request.json['num2'])
            if operation == 'add':
                r = num1 + num2
                result = 'The sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            elif operation == 'subtract':
                r = num1 - num2
                result = 'The difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            elif operation == 'multiply':
                r = num1 * num2
                result = 'The product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            elif operation == 'divide':
                r = num1 / num2
                result = 'The quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
            else:
                result = 'Please specify valid operation'
            return jsonify(result)
        except Exception as e:
            result = "An Exception "+str(e)+" Occurred"
            return jsonify(result)


if __name__ == '__main__':
    print('The app_calc is running')
    app_calc.run()