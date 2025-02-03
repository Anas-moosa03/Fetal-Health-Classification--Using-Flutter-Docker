from flask import Flask, render_template, request, redirect, url_for, jsonify
import pickle
import numpy as np
import pandas as pd
import os
app = Flask(__name__)


model = pickle.load(open('finalized_model.sav', 'rb'))
scaler = pickle.load(open("scaler.sav", 'rb'))




@app.route('/')
def home():
    return render_template('home.html')

@app.route('/eda')
def eda():
    return render_template('eda.html')



@app.route('/predictions', methods=['GET', 'POST'])
def predictions():
    result = ""
    feature_names = ['Baseline', 'Accelerations', 'Fetal Movement','Uterine Contractions','Light Decelerations','Severe Decelerations','Prolongued Decelerations','Abnormal Short Term Variability','Mean Short Term Variability','Time With Abnormal Long Term Variability','Mean Long Term Variability','Histogram Width','Histogram Min','Histogram Max','Histogram Number of Peaks',	'Histogram Number of Zeroes',	'Histogram Mode',	'Histogram Mean',	'Histogram Median',	'Histogram Variance',	'Histogram Tendency']
    if request.method == 'POST':
        try:
            inputs = [float(request.form[f'input{i}']) for i in range(1, 22)]
            inputs_arr = np.array(inputs).reshape(1, -1)
            scaled_inputs = scaler.transform(inputs_arr)
            prediction = model.predict(scaled_inputs)
            result = str(prediction[0])
        except Exception as e:
            result = str(e)
    if result == "1.0":
        result = "Normal"
    elif result == "2.0":
        result = "Suspect"
    else:
        result = "Pathological"
    return render_template('predictions.html', feature_names=feature_names, result=result)

def model_predict(inputs):
    # Replace this with your actual model prediction logic
    return sum(inputs)  # Example placeholder




@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)