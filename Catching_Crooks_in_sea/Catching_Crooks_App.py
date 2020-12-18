from flask import Flask, render_template, request
import pickle
import numpy as np
import os


model = pickle.load(open('catching_crooks.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')

def main():
    return render_template('Catching_Crooks.html')

@app.route('/predict', methods=['POST'])
def predict():
    data1 = request.form['active-2012']
    data2 = request.form['active-2013']
    data3 = request.form['active-2014']
    data4 = request.form['active-2015']

    if data1.lower() == 'yes':
        data1 = 1
    else:
        data1 = 0

    if data2.lower() == 'yes':
        data2 = 1
    else:
        data2 = 0

    if data3.lower() == 'yes':
        data3 = 1
    else:
        data3 = 0
        
    if data4.lower() == 'yes':
        data4 = 1
    else:
        data4 = 0

    x_DT = np.array([[data1, data2, data3, data4]])
    x_DT_prediction = model.predict(x_DT)

    if x_DT_prediction == 1:
        return render_template('Catching_Crooks.html', pred = "Ship will be sailing in 2016")
    else:
        return render_template('Catching_Crooks.html', pred= "Ship will not be sailing in 2016")
    


if __name__ == "__main__":
    app.run(debug = True)

    
