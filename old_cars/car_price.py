from flask import Flask, jsonify,render_template,request
import pickle

app = Flask(__name__)

@app.route('/')
def fun1():
    return render_template ('car.html')

@app.route('/predict',methods=['POST'])
def fun2():
    company_model = str(request.form.get('modelName'))
    company = str(request.form.get('company'))
    year = int(request.form.get('year'))
    kilometers = int(request.form.get('kilometers'))
    fuel_type = str(request.form.get('fuelType'))
    model = pickle.load(open('pipe1.pkl','rb'))
    prd = model.predict([[company_model,company,year,kilometers,fuel_type]])
    predicted_price = prd[0]
    return jsonify({'predicted_Price': int(predicted_price)})


if __name__ == '__main__':
    app.run(debug=True)