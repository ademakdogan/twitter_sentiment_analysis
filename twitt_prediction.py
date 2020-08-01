#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 14:13:00 2020

@author: A.Akdogan
"""
import os
import pickle
import argparse



class TwittPrediction():
    
    def load_model(self):
        model_path  = os.path.join(os.path.dirname(os.path.realpath(__file__)), "model/twit_model.sav")
        model = pickle.load(open(model_path, "rb"))
        return model
    
    def load_tfidf(self):
        tf_path  = os.path.join(os.path.dirname(os.path.realpath(__file__)), "model/tfidf.sav")
        tfidf = pickle.load(open(tf_path, "rb"))
        return tfidf
    
    def prediction_part(self, twitt, model, tfidf):
        a = [twitt]
        result = model.predict(tfidf.transform(a))
        if result == 0:
            text = "Negative"
        else:
            text = "Positive"
        return text 
 
       
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--text", required=True,
    	help="Path")


    args = vars(ap.parse_args())
    
    t_pred = TwittPrediction()
    model = t_pred.load_model()
    tfidf = t_pred.load_tfidf()
    text = t_pred.prediction_part(args["text"], model, tfidf)
    print(text)

