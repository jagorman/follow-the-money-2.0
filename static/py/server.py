import predict
from tensorflow.keras.models import load_model
from flask import Flask
from flask_cors import CORS, cross_origin

model = load_model('contributor_model.h5')


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={
            r"/<params>": {"origins": "http://localhost:port"}})


@app.route('/')
def home():
    return 'REST'


@app.route("/<params>")
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def index(params):
    prediction = predict.predict(params)
    return prediction


if __name__ == "__main__":
    app.run(debug=True)
