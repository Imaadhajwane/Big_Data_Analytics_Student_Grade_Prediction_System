from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained Random Forest model and scaler
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input features from the form
    try:
        age = float(request.form['age'])
        studytime = float(request.form['studytime'])
        failures = float(request.form['failures'])
        Medu = float(request.form['Medu'])
        G1 = float(request.form['G1'])
        G2 = float(request.form['G2'])

        # Prepare the input data for prediction
        input_data = np.array([[age, studytime, failures, Medu, G1, G2]])

        # Scale the features using the loaded scaler
        input_data_scaled = scaler.transform(input_data)

        # Make a prediction
        prediction_proba = model.predict_proba(input_data_scaled)

        # Ensure prediction_proba has valid values
        if prediction_proba is not None and len(prediction_proba) > 0:
            # Get the probability of passing
            probability_of_pass = prediction_proba[0][1]  # Probability of passing
            probability_of_pass = round(probability_of_pass, 2)  # Round for display

            # Determine Pass/Fail based on the probability threshold
            result = "Pass" if probability_of_pass > 0.75 else "Fail"

            return render_template('result.html', result=result, probability=probability_of_pass)
        else:
            # Handle the case where prediction_proba is not valid
            return render_template('result.html', result="Error", probability=0.0)

    except ValueError as e:
        # Handle the case where input conversion fails
        return render_template('result.html', result="Error", probability=0.0)

if __name__ == '__main__':
    app.run(debug=True)
