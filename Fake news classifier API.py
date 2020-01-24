# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 19:15:32 2020

@author: Abhimanyu
"""
import pandas as pd
import numpy as np
import pickle
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
    json = request.json
    dataset = pd.DataFrame(json, index=[0])
    #parsing URLs
    '''from urllib.parse import urlparse
    for i in range(len(dataset)):
        dataset['URLs'][i]= urlparse(dataset.values[i,0]).netloc'''

    X = dataset.iloc[:,:].values
    


    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    import re
    ps = PorterStemmer()
    for i in range(len(dataset)):
        X[i][1] = ' '.join([ps.stem(word) for word in re.sub('[^a-zA-Z]', ' ', X[i][1]).lower().split() if not word in stopwords.words('english')])
        X[i][2] = ' '.join([ps.stem(word) for word in re.sub('[^a-zA-Z]', ' ', X[i][2]).lower().split() if not word in stopwords.words('english')])
        
        
        
    mat_body = cv_body.transform(X[:,2]).todense()
    mat_head = cv_head.transform(X[:,1]).todense()
    #mat_url = cv_url.transform(X[:,0]).todense()
        
    #X_mat = np.hstack((mat_url, mat_head, mat_body))
    X_mat = np.hstack((mat_head, mat_body))
        
        
    y_pred = classifier_dtr.predict(X_mat)
        
    return jsonify({'Prediction' : 'Genuine' if (y_pred[0] == 1) else 'Fake'})
        



if __name__ == '__main__':
    cv_body = pickle.load(open("cv_body.pkl",'rb'))
    cv_head = pickle.load(open("cv_head.pkl",'rb'))
    #cv_url = pickle.load(open("cv_ulr.pkl",'rb'))
    import joblib
    classifier_dtr = joblib.load('classifier_dtr_fakenews_nourl.pkl')
    app.run(debug=True, use_reloader=False)
    

