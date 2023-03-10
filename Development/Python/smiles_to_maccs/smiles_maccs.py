from rdkit.Chem import MolFromSmiles
from rdkit.Chem import MACCSkeys
import pandas as pd
from typing import *

smile_test = 'c1c(CCO)ncnc1C(=O)O'

def smiles_maccs(smiles_input: str) -> dict:
    '''
    description : function to calculate maccs keys from smiles
    input: smiles
    output: string of MACCS keys
    '''

    macc_bits = 167
    maccs_fp_name = [f'maccs_{i}' for i in range(macc_bits)] # generate generic fingerprint names for maccs

    mol= MolFromSmiles(smiles_input)  # generate mol objects from SMILE

    maccs_fp= MACCSkeys.GenMACCSKeys(mol)  # # get maccs fingerprints
    maccs_fp_bits = list(maccs_fp) 
 
    df_maccs = pd.DataFrame(data=[maccs_fp_bits]) # generate dataframe from maccs numeric bits
    df_maccs.columns = maccs_fp_name # map descriptor names to the columns

    df_maccs= df_maccs.iloc[:,1:] # dropping dummy first bit (always 0)
    #df_maccs_json = df_maccs.iloc[0].to_json() # create json from first row (only 1 row in data frame)
    
    return(df_maccs)

def get_maccs_from_smiles(smiles_input: str) -> np.array:
    '''
    description : function to calculate maccs keys from a smile string
    input: smiles
    output: string of MACCS keys
    '''
    mol= MolFromSmiles(smiles_input)  # generate mol objects from SMILE

    maccs_fp= MACCSkeys.GenMACCSKeys(mol)  # # get maccs fingerprints
    maccs_fp_array= np.array(list(
        maccs_fp)[1:]) # removing the first bit which is always zero
    mmaccs_fp_array_reshaped= maccs_fp_array.reshape(1,-1) # reshape to be accepted my model
    return(mmaccs_fp_array_reshaped)