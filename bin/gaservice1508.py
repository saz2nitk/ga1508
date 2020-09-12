# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 15:45:48 2020

@author: saz2n
"""

import flask
from flask import request, Flask
from summariserga import FindSummary
import json

app = Flask(__name__)

#removed bugs
@app.route('/home',methods=['GET'])
def checkApiStatus():
    return "Yay!! Its all good"

@app.route('/get_summary',methods=['POST'])
def summarise():
    article = json.loads(request.data.decode())['article']
    summaryObj = FindSummary('config/config')
    summaryText = summaryObj.summarise(article)
    return summaryText

@app.route('/about_us',methods=['POST'])
def dummyReq():
#    jsonStr = request.data.decode()
#    dataDict = json.loads(jsonStr)
#    article = dataDict['article']
    article = json.loads(request.data.decode())['article']
    print('Printing data:\n',article)
    return "Ok request works"

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)