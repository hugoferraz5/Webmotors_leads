import os
import pickle
import json
import pandas as pd
from flask import Flask, request, Response, jsonify
from webmotors.Webmotors import Webmotors

# loading model
model = pickle.load( open( 'Models/rfc_tuned_model.pkl', 'rb') )

# initialize API
app = Flask( __name__ )

@app.route('/predict', methods=['POST'])
def predict():
    test_json = request.get_json()
    
    if test_json: # there is data
        if isinstance(test_json, dict): # unique example
            test_raw = pd.DataFrame.from_dict([test_json])  # Convert dictionary to DataFrame
            
        else: # multiple example
            test_raw = pd.DataFrame(test_json)
            
        # Instantiate Webmotors class
        pipeline = Webmotors()
        
        # data preparation
        df1 = pipeline.data_preparation(test_raw)
        
        # prediction
        df_response = pipeline.get_prediction(model, test_raw, df1)
        
        return Response(response=df_response, status=200, mimetype='application/json')
    else:
        return jsonify([]), 200

if __name__ == '__main__':
    port = os.environ.get('PORT',5000)
    app.run( host='0.0.0.0', port=port )
