from flask import Flask, render_template, request
import numpy as np 

from predictions import predict 

app = Flask(__name__)


@app.route('/')
def home(): 
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict_route(): 
    if request.method == 'POST': 
        age = request.form['age']
        PClass = request.form['PClass']
        Fare = request.form['Fare']
        Embarkment = request.form['Embarkment']

        # convert input data into the correct format for prediction 
        input_data = np.array([[int(age), int(PClass), int(Fare), int(Embarkment)]])

        # make prediction using the predict() function 
        result = predict(input_data)

        # display the prediction 
        return render_template('result.html', prediction=result[0])
    else: 
        return render_template('home.html')
    

if __name__ == "__main__": 
    app.run(debug=True)
