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

@app.route('/home',methods=['GET'])
def checkApiStatus():
    return "Yay!! Its all good"

@app.route('/get_summary',methods=['GET'])
def summarise():
    summaryObj = FindSummary('config/config')
    summaryText = summaryObj.summarise()
    return summaryText

if __name__=="__main__":
    app.run(host='127.0.0.1',port=5000,debug=True)