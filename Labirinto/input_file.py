# -*- coding: utf-8 -*-
"""
Created on Tue May 23 13:41:20 2023

"""
import json
from PIL import Image
import numpy as np

class Input_file:
    
    """
    Classe che implementa e gestisce l'input
    
    Il programma riceve in ingresso:
        - il file, in formato .json o .tiff
        - il/i punto/i di partenza e arrivo
        
    """
    
    
        
        
    def leggi_file_json(self, filepath):
        """

        Parameters
        ----------
        filepath : str
            prende in ingresso il path del file da leggere in formato json

        Returns
        -------
        dictionary : dict
            restituisce un dizionario che contiene le caratteristiche del labirinto
        
        """
        
        with open(filepath) as file:
            dictionary = json.load(file)
        return dictionary 
    
    
    def leggi_file_tiff(self,filepath):
        
        """
        
        Parameters
        ----------
        filepath : str
            prende in ingresso il path del file da leggere in formato .tiff

        Returns
        -------
        img_array : array
        
            restituisce l'immagine contenuta nel file attraverso un array tridimensionale, nel quale le tre 
            dimensioni corrispondono all'altezza, alla larghezza e ai canali dell'immagine.
            
            Essendo l'immagine a colori, l'array ha forma: (altezza, larghezza, 3), perchè si hanno 3 
            canali per i colori (RGB) 

        """
     
        with Image.open(filepath) as img:
            # Converte l'immagine in una matrice NumPy
            img_array = np.array(img)
            return img_array
        
    
    
