# -*- coding: utf-8 -*-
"""
Created on Tue May 23 13:41:20 2023

"""
import os
import json
import numpy as np

from PIL import Image
from Labirinto import Labirinto


class Input_file:
    
    """
    Classe che implementa e gestisce l'input
    
    Il programma riceve in ingresso:
        - il file, in formato .json o .tiff
        - il/i punto/i di partenza e arrivo
        
    """
    
    def leggi_file(self, filepath):
       
        """
        Metodo che restituisce il labirinto sotto forma di dizionario o array, in base
        al formato del file di input (.json o .tiff)

        Parameters
        ----------
        filepath : str
            prende in ingresso il path del file da leggere in formato json

        Returns
        -------
        dictionary : dict, img_arry
            
        """
        percorso,estensioneFile = os.path.splitext(filepath)
        if estensioneFile == '.json':
            dictionary=Input_file.leggi_file_json(self,filepath)
            maze=Labirinto()
            (labirinto, partenze, destinazioni)=maze.crea_labirinto_json(dictionary)
            return (labirinto, partenze, destinazioni)
        elif estensioneFile == '.tiff':
            img_array =Input_file.leggi_file_tiff(self, filepath)
            return img_array
        
        
    def leggi_file_json(self, filepath):
       
        """
        Metodo che restituisce il dizionario contenente le caratteristiche del labirinto

        Parameters
        ----------
        filepath : str
            prende in ingresso il path del file da leggere in formato json

        Returns
        -------
        dictionary : dict
        
        """
        
        with open(filepath) as file:
            dictionary = json.load(file)
        return dictionary 
    
    
    def leggi_file_tiff(self,filepath):
        
        """
        Metodo che restituisce l'immagine contenuta nel file attraverso un array tridimensionale, nel quale le tre 
        dimensioni corrispondono all'altezza, alla larghezza e ai canali dell'immagine.
        
        Essendo l'immagine a colori, l'array ha forma: (altezza, larghezza, 3), perchè si hanno 3 
        canali per i colori (RGB)
        
        
        Parameters
        ----------
        filepath : str
            prende in ingresso il path del file da leggere in formato .tiff

        Returns
        -------
        img_array : array
        
        """
     
        with Image.open(filepath) as img:
            # Converte l'immagine in una matrice NumPy
            img_array = np.array(img)
            return img_array
        
    
    
