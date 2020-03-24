from flask import request
from flask import jsonify
from flask import Flask,render_template
import base64
import io
from predict import *
app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    print("page loaded")
    if request.method == "POST":
        print ("request recieved")
        message = request.get_json(force=True)
        encoded = message['image']
        encoded = encoded.partition(",")[2]

        decoded = base64.b64decode(encoded)

        preprocessed_image = preprocess_image(decoded)
    

        prediction = make_prediction(preprocessed_image)
        prediction = np.array(prediction)
        probability = np.max(prediction)*100.0
        number = np.argmax(prediction)
        if probability > 60:
            #print("you entered number : " + str(number))
            return str(number)
        else:
            #print('enter a valid number')
            return str(0)
        
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)

