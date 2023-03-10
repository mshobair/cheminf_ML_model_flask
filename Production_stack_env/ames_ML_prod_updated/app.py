import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib
from rdkit.Chem import MolFromSmiles
from rdkit.Chem import MACCSkeys



app = Flask(__name__)
model = joblib.load('rf_bal_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

def get_maccs_from_smiles(smiles_input: str) -> np.array:
    '''
    description : function to calculate maccs keys from smiles
    input: smiles
    output: string of MACCS keys
    '''
    mol= MolFromSmiles(smiles_input)  # generate mol objects from SMILE

    maccs_fp= MACCSkeys.GenMACCSKeys(mol)  # # get maccs fingerprints
    maccs_fp_array= np.array(list(
        maccs_fp)[1:]) # removing the first bit which is always zero
    maccs_fp_array_reshaped= maccs_fp_array.reshape(1,-1) # reshape to be accepted my model
    return(maccs_fp_array_reshaped)

@app.route('/predict',methods=['POST'])
def predict():

    smiles_input_str = [str(x) for x in request.form.values()][0]
    
    prediction = model.predict_proba(
        get_maccs_from_smiles(smiles_input_str)
    )
    # output formatting
    probability_result= prediction.ravel()[1]
    # assign binary call
    if probability_result >= 0.5:
        pos_neg_result= 'Positive'
    else:
        pos_neg_result= 'Negative'
    return render_template('index.html', prediction_text='Ames activity expected to be {}, with probability {}'.format(pos_neg_result, probability_result))

# method to get results  

@app.route('/ames_prediction/<SMILES>')
def get_ames_prediction(SMILES: str) -> str:
    # Run prediction method
    SMILES_input= str(SMILES)
    prediction = model.predict_proba(
        get_maccs_from_smiles(SMILES_input)
    )
    # output formatting
    probability_pos_result= prediction.ravel()[1]
 
    return jsonify(probability_pos_result)


@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict(
        get_maccs_from_smiles(data)
    )


    output = prediction
    return jsonify(output)

if __name__ == "__main__":
    app.run(host= '137.183.11.247', debug=True)