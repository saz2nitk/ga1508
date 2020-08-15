# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:47:37 2020

@author: saz2n
"""
import yaml
import numpy as np
from preprocessor import PreprocessText

class FindSummary:
    
    def __init__(self,configPath):
        with open(configPath,'r') as fl:
            self.config = yaml.load(fl)

    def loadData(self):
        with open(self.config['data']['articles_path']) as fl:
            articleText = fl.read()
        return articleText
            
    def splitSentence(self,text):
        """
        Split sentences using full stop
        
        Inputs:
            text: string
        Outputs:
            sentences: List
        """
        sentences = text.split('.')
        return sentences
    
    def groupSentence(self,sentences):
        """
        Group sentences into first and rest
        
        Input:
            sentences: List or strings
        Output:
            text1: string
            remainingText: List of string
        """
        text1 = sentences[0]
        remainingText = sentences[1:]
        return text1,remainingText
    
    def findSentLen(self,sentences):
        sentLenghts = [len(sent) for sent in sentences]
        return sentLenghts
    
    def findTopFive(self,sentences,sentLengths):
        sortedIdx = np.argsort(sentLengths)
        top5idx = sortedIdx[-5:]
        top5Sents = [sentences[i] for i in top5idx]
        return top5Sents
        
    def summarise(self):
        
        articleText = self.loadData()
        preprocessObj = PreprocessText()
        loweredText = preprocessObj.convertToLower(articleText)
        filteredText = preprocessObj.removeSpecialChar(loweredText)
        sentences = self.splitSentence(filteredText)
        text1,remainingText = self.groupSentence(sentences)
        sentLengths = self.findSentLen(remainingText)
        top5Sents = self.findTopFive(remainingText,sentLengths)
        summaryTextList = [text1]
        summaryTextList.extend(top5Sents)
        summaryText = ' '.join(summaryTextList)
        return summaryText
    
if __name__=="__main__":
    summaryObj = FindSummary('../config/config')
    summaryText = summaryObj.summarise()
        
    
    