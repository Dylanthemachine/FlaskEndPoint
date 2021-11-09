from flask import Flask
import pandas as pd
import json

app = Flask(__name__)

df = pd.read_csv('takedown08112021191500.csv')
test = json.dumps(df.to_dict())

@app.route("/takedown")
def endPoint():
    return test

if __name__ == "__main__":
    app.run()
