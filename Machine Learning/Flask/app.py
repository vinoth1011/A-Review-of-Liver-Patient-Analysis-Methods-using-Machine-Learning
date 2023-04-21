from flask import Flask, render_template, request
import numpy as np
import pickle
import os


app=Flask(__name__)
@app.route('/')
def home():
  return render_template('home.html')
@app.route('/predict')
def index():
 return render_template("index.html")

@app.route('/data_predict',methods=['POST'])
def predict():
    age = request.form['age']
    gender=request.form['gender']
    tb = request.form['tb']
    db = request.form['db']
    ap = request.form['ap']
    aa1 = request.form['aa1']
    aa2 = request.form['aa2']
    tp = request.form['tp']
    a = request.form['a']
    agr = request.form['agr']

    data = [[float(age),float(gender),float(db),float(ap),float(aa1),float(aa2),float(tp),float(a),float(agr)]]
    model=pickle.load(open(os.path.join('c:Users/91630/Desktop/liver patient/Liver Patient Analysis/Flask app,pkl_objects','liver_analysis_1.pkl'),'rb'))

  
    prediction= model.predict(data)[0]
    if (prediction == 1):
      return render_template('noChance.html',prediction='You have a liver desease problem,You must and should consult a doctor.Take care')
    else:
      return render_template('chance.html', prediction='You dont have a liver desease problem')

if __name__ =='__main__':
    app.run(debug=True)
