#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 00:32:01 2020

@author: A.Akdogan
"""
import re
import contractions
import string



def remove_mention(text):
    text = re.sub(r"@[A-Za-z0-9]+","",text)
    return text

def remove_rt(text):
    text = re.sub("RT[/s]+","",text)
    return text

def text_lower(text):
    text = text.lower()
    return text

def cont_text(text):
    text = contractions.fix(text)
    return text

def remove_http(text):
    text_list = text.split()
    temp_list = []
    for t in text_list:
        if re.search("http", t):
            pass
        else:
            temp_list.append(t)
    text = " ".join(temp_list)
    return text

def remove_mail(text):
    text = re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"", text)
    return text
    
def remove_special_char(text):
    text = re.sub(r'[^\w ]+', "", text)
    return text

def clean_data(text):
    remove_list = ["-", "_", "/", "\\", "# ", "!"]
    for i in range(len(remove_list)):
        text = text.replace(remove_list[i], " ")
    
    return text