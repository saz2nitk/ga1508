# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:46:58 2020

@author: saz2n
"""
import re

class PreprocessText:
    """
    Preprocess articles fed from files
    """
    
    def __init__(self):
        pass
    
    def convertToLower(self,text):
        """
        Convert text to lowercase
        
        Input:
            text: string
        Output:
            text:string
        """
        loweredText = text.lower()
        return loweredText
    
    def removeSpecialChar(self,text):
        """
        """
        processedText = re.sub(',|;|<|>|','',text)
        return processedText

#if __name__=="__main__":
#    preprocessObj = PreprocessText()
#    text = "Jamaican Foreign Minister Kamina Smith had wished Ms. Harris on her “historic selection” in a tweet."
#    loweredText = preprocessObj.convertToLower(text)
#    filteredText = preprocessObj.removeSpecialChar(loweredText)
#    print('filtered text: {}'.format(filteredText))
    
    