from flask import Flask,render_template,request,jsonify
import pickle

app = Flask(__name__)

@app.route('/')
def fun():
    return render_template('dia.html')

@app.route('/predict',methods=['POST'])
def fun2():
    pregnencies = int(request.form.get('pregnancies'))
    glucose = float(request.form.get('glucose'))
    bloodPressure = float(request.form.get('bloodPressure'))
    skinThickness = float(request.form.get('skinThickness'))
    insulin = int(request.form.get('insulin'))
    bmi = float(request.form.get('bmi'))
    diabetesPedigreeFunction = float(request.form.get('diabetesPedigreeFunction'))
    age = int(request.form.get('age'))
    mymodel = pickle.load(open('model_diab.pkl','rb'))
    Dia = mymodel.predict([[pregnencies,glucose,bloodPressure,skinThickness,insulin,bmi,diabetesPedigreeFunction,age]])
    predicted_Diabetes = Dia[0] 
    return jsonify({'Prediction of Diabetese is: ': int(predicted_Diabetes)})



if __name__ == '__main__':
    app.run(debug=True)