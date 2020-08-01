#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 12:20:08 2020

@author: A.Akdogan
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import sys,os

import pickle
import argparse
from sklearn.ensemble import RandomForestClassifier
parent_dir = os.getcwd() # find the path to module a
# Then go up one level to the common parent directory
path = os.path.dirname(parent_dir)
# Add the parent to sys.pah
sys.path.append(path)
import nlp_preprocess as nlp
from sklearn.model_selection import GridSearchCV

class Twitts():
    def __init__(self, path, tuning):
        self.df = pd.read_csv(path)

        
    def preprocess(self):
        self.df["new_tw"] = self.df["twitts"].apply(nlp.remove_mention)
        self.df["new_tw"] = self.df["new_tw"].apply(nlp.remove_rt)
        self.df["new_tw"] = self.df["new_tw"].apply(nlp.text_lower)
        self.df["new_tw"] = self.df["new_tw"].apply(nlp.cont_text)
        self.df["new_tw"] = self.df["new_tw"].apply(nlp.remove_http)
        self.df["new_tw"] = self.df["new_tw"].apply(nlp.remove_mail)
        self.df["new_tw"] = self.df["new_tw"].apply(nlp.clean_data)
        return self.df
    
    def training_part(self, df):
        print("The training process has started!")
        X = df["new_tw"]
        y = df["sentiment"]
        tfidf = TfidfVectorizer()
        X = tfidf.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20 , random_state = 30)
        rf = RandomForestClassifier()
        model = rf.fit(X_train, y_train)
        #y_pred = model.predict(X_test)
        #print(classification_report(y_test, y_pred))
        model_path  = os.path.join(os.path.dirname(os.path.realpath(__file__)), "model/twit_model.sav")
        tf_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "model/tfidf.sav")
        pickle.dump(model, open(model_path, 'wb'))
        pickle.dump(tfidf, open(tf_path, 'wb'))
        print("The training process completed!")
        
    def tuning_part(self, df):
        print("The training process has started! (Model tuning)")
        X = df["new_tw"]
        y = df["sentiment"]
        tfidf = TfidfVectorizer()
        X = tfidf.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20 , random_state = 30)
        rf_params = {"max_depth": [None, 2,5,9],
                     "n_estimators": [10,100,500,1000],
                     "max_features": ["auto",3,5]}


        model = RandomForestClassifier()
        grid_search  = GridSearchCV(estimator = model,
                                    param_grid = rf_params,
                                    scoring = "accuracy",
                                    cv = 10,
                                    n_jobs  = -1)
        grid_search  = grid_search.fit(X_train, y_train)
        model_path  = os.path.join(os.path.dirname(os.path.realpath(__file__)), "model/twit_model.sav")
        tf_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "model/tfidf.sav")
        pickle.dump(grid_search, open(model_path, 'wb'))
        pickle.dump(tfidf, open(tf_path, 'wb'))
        print("The training process completed! (Model tuning)")
            
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required=True,
    	help="Path")
    ap.add_argument("-t", "--tuning", type = bool, default= False,
    	help="Turn to True for model tuning")

    args = vars(ap.parse_args())
    twitt = Twitts(args["path"], args["tuning"])
    df = twitt.preprocess()
    if args["tuning"] == False:
        
        
        twitt.training_part(df)
        
    else:
        twitt.tuning_part(df)
    
   
