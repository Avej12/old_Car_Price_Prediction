from flask import Flask,render_template,request,jsonify
import pickle

app= Flask(__name__)

@app.route('/')
def fun1():
    return render_template('ins.html')

@app.route('/predict',methods=['POST'])
def fun2():
    age = int(request.form.get('age'))
    sex = int(request.form.get('sex'))
    bmi = float(request.form.get('bmi'))
    children = int(request.form.get('children'))
    smoker = int(request.form.get('smoker'))
    mymodel = pickle.load(open('model_H_Ins.pkl','rb'))
    Ins = mymodel.predict([[age,sex,bmi,children,smoker]])
    predicted_Insurance = Ins[0] 
    return jsonify({'predicted_Insurance': predicted_Insurance})


if __name__ == '__main__':
    app.run(debug=True)