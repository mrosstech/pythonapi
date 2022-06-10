import os
import glob
import json
import pandas as pd
from flask import Flask, request
app = Flask(__name__)

# define file locations:
data_dir = os.path.join(app.instance_path, 'data')
os.makedirs(data_dir, exist_ok=True)

@app.route('/datasets/', methods=['GET'])
def getDatasets():
    # Get all files with the pkl extension in the data directory
    datasets = glob.glob(data_dir + "/*.pkl")
    return json.dumps(datasets)

@app.route('/datasets/', methods=['POST'])
def postDatasets():
    csvFile = request.files['file']
    if csvFile:
        df = pd.read_csv(csvFile)
        df.to_pickle(os.path.join(data_dir, csvFile.filename + ".pkl"))
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 




