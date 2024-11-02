from flask import Flask,render_template,request,jsonify
import pickle

app= Flask(__name__)

@app.route('/')
def fun1():
    return render_template('heart.html')

@app.route('/predict',methods=['POST'])
def fun2():
    age = int(request.form.get('age'))
    sex = int(request.form.get('sex'))
    cp = float(request.form.get('cp'))
    trestbps = float(request.form.get('trestbps'))
    chol = float(request.form.get('chol'))
    fbs = float(request.form.get('fbs'))
    restecg = float(request.form.get('restecg'))
    thalach = float(request.form.get('thalach'))
    exang = float(request.form.get('exang'))
    oldpeak = float(request.form.get('oldpeak'))
    slope = float(request.form.get('slope'))
    ca = float(request.form.get('ca'))
    thal = float(request.form.get('thal'))
    scaler = pickle.load(open('scaler_Hrt.pkl','rb'))
    scaler.transform([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    model = pickle.load(open('model_Hrt.pkl','rb'))
    prd = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    predicted_disease = prd[0]
    return jsonify({'predicted_disease': int(predicted_disease)})



if __name__ == '__main__':
    app.run(debug=True)