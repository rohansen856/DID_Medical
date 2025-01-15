
from flask import Flask, jsonify, request
import flask_cors

from lib import ocr,meds,cert,recommendation

app = Flask(__name__)
flask_cors.CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/get_meds_ocr", methods=["POST"])
def get_meds_ocr():
    data = request.get_json()
    img_data = data.get('img')
    text = ocr.do_ocr(img_data)
    
    return meds.post_process_meds(text)

@app.route("/verify_cert", methods=["POST"])
def verify_cert():
    data = request.get_json()
    img_data = data.get('img')
    doc_dob = data.get('dob')
    doc_reg_no = data.get('reg_no')
    doc_name = data.get('name')
    text = ocr.do_ocr(img_data)
    doc_cert = cert.post_process_cert(text)

    if doc_cert['name'] == doc_name and doc_cert['dob'] == doc_dob and doc_cert['reg_no'] == doc_reg_no:
        return {"verified": True}
    else:
        return {"verified": False}
    
@app.route("/get_recommendation", methods=["POST"])
def get_recommendation():
    data = request.get_json()
    problem = data.get("problem")
    
    if not problem:
        return jsonify({"error": "Please provide a problem description."}), 400
    response = recommendation.recommend_doctor(problem)
    
    if isinstance(response, tuple):  
        return jsonify(response[0]), response[1]
    
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)