from flask import Flask,request,jsonify
import numpy as np
import pickle
from sklearn import preprocessing

model = pickle.load(open('diabetics.pkl','rb'))

app = Flask(__name__)


@app.route('/diabetic',methods=['POST'])
def diabetic():

    pregnancies=request.form.get('Pregnancies')
    glucose=request.form.get('glucose')
    bp=request.form.get('bp')
    skin=request.form.get('skin')
    insulin=request.form.get('insulin')
    bmi=request.form.get('bmi')
    pedigree=request.form.get('pedigree')
    age=request.form.get('age')

    list = [pregnancies,glucose,bp,skin,insulin,bmi,pedigree,age]

    #print(list)
    #from sklearn.preprocessing import LabelEncoder
    #le = LabelEncoder()
   # li = le.fit_transform(list)

    result = model.predict([list])[0]

    return jsonify({'disease': str(result)})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
