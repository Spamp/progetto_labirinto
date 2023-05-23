# -*- coding: utf-8 -*-
"""
Created on Tue May 23 13:41:20 2023

"""
import json

class Input_file:
    
    """
    Classe che implementa e gestisce l'input
    
    Il programma riceve in ingresso:
        - il file, in formato .json o .tiff
        - il/i punto/i di partenza e arrivo
        
    """
    
    
        
        
    def leggi_file_json(self, filepath):
        with open(filepath) as file:
            dictionary = json.load(file)
        return dictionary 
        
        
    
    
