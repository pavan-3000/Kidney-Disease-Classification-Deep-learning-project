from flask import Flask,jsonify,render_template,request
from flask_cors  import CORS,cross_origin
from src.project.pipeline.prediction import PredictPipeline
from src.project.utils.common import decodeImage
import os
app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictPipeline(self.filename)
        
@app.route("/",methods=["Get"])
@cross_origin()
def home():
    return render_template("index.html")

@app.route('/train',methods=['GET','POST'])
@cross_origin()
def train():
    os.system("python main.py")
    return "Trainig done sucessfully"

@app.route("/predict",methods=['POST'])
@cross_origin()
def predict():
    image = request.json['image']
    decodeImage(image,clApp.filename)
    result = clApp.classifier.Predict()
    return jsonify(result)
    
    

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0')