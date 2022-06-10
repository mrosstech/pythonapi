import os
import glob
import pandas as pd
from flask import Flask, request
app = Flask(__name__)

# define file locations:
data_dir = os.path.join(app.instance_path, 'data')
os.makedirs(data_dir, exists_ok=True)

@app.route('/datasets/', methods=['GET'])
def getDatasets():
    # Get all files with the pkl extension in the data directory
    datasets = glob.glob(data_dir + "/*.pkl")
    return datasets

@app.route('/datasets/', methods=['POST'])
def postDatasets():
    csvFile = request.files['file']
    if csvFile:
        df = pd.read_csv(csvFile)
        df.to_pickle(os.path.join(data_dir, csvFile.filename + ".pkl"))




