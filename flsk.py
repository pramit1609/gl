# Import necessary libraries
from flask import Flask, request, Response
from joblib import load
import numpy as np
# Load the pre-trained Logistic Regression model
my_lr_mod = load("Model/irispred.joblib")
# Initializing
app = Flask(__name__)

# Endpoint for handling predictions
@app.route("/predictions", methods=['POST', 'GET'])
def predictions():
    data = request.json

    user_sent_this_data = data.get('mydata')
    user_number = np.array(user_sent_this_data).reshape(1, -1)

    model_prediction = my_lr_mod.predict(user_number)

    # returning the response
    return Response(str(model_prediction))

# Main script execution
if __name__ == '__main__':
    app.run(debug=True)
