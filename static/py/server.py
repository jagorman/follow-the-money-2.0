import predict
from tensorflow.keras.models import load_model
from flask import Flask

model = load_model('contributor_model.h5')


app = Flask(__name__)


@app.route('/')
def home():
    return 'REST'


@app.route("/<params>")
def index(params):
    prediction = predict.predict(params)
    return prediction


if __name__ == "__main__":
    app.run(debug=True)
