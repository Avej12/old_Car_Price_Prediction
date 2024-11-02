from flask import Flask,render_template,request,jsonify
import pickle

app = Flask(__name__)

@app.route('/')
def fun1():
    return render_template('info.html')

@app.route('/predict',methods=['POST'])
def fun2():
    name = request.form['name']
    exp = float(request.form['exp'])
    mymodel = pickle.load(open('model1.pkl','rb'))
    sal = mymodel.predict([[exp]])
    predicted_salary = sal[0] 
    return jsonify({'name': name, 'predicted_salary': predicted_salary})
    


if __name__ == '__main__':
    app.run(debug=True)