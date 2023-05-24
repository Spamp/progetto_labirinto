# -*- coding: utf-8 -*-
"""
Created on Tue May 23 13:51:57 2023

"""
import numpy as np

class Labirinto:
    """
    Classe che implementa il labirinto
    
    """

    def crea_labirinto_json(self,dict):
        """
        inpunt: dizionario con caratteristiche del labirinto

        metodo che crea il labirito sostituendo nelle coordinate specificate nel dizionario i costi corrispondenti 
        e pone al posto delle pareti il valore nan.
        inoltre salva in una lista di liste le posizioni di partenza e di destinazione.

        output: matrice labirinto, lista delle posizioni di partenza e lista delle posizioni di destinazione
        """
        #creo una matrice numpy piena di zeri, con le grandezze del labirinto
        labirinto= np.full((dict['altezza'], dict['larghezza']), 1.)
        partenze=dict['iniziali']
        destinazioni=dict['finale']
        #creo le pareti sostiuendo gli zeri con nan
        for i in range(len(dict['pareti'])):
            if dict['pareti'][i]['orientamento']=='H':
                indice1=int(dict['pareti'][i]['posizione'][0])
                indice2=int(dict['pareti'][i]['posizione'][1])
                indice3=int(dict['pareti'][i]['posizione'][1])+int(dict['pareti'][i]['lunghezza'])
                labirinto[indice1,indice2:indice3]=np.nan
            else:
                indice1=int(dict['pareti'][i]['posizione'][0])
                indice2=int(dict['pareti'][i]['posizione'][0])+int(dict['pareti'][i]['lunghezza'])
                indice3=int(dict['pareti'][i]['posizione'][1])
                labirinto[indice1:indice2,indice3]=np.nan
        #sostuisco con il costo le posizioni specificate
        for i in range(len(dict['costi'])):
            posizione_orizzontale=dict['costi'][i][0]
            posizione_verticale=dict['costi'][i][1]
            labirinto[posizione_orizzontale,posizione_verticale]=float(dict['costi'][i][2])
        return (labirinto, partenze, destinazioni)
    
    
    def crea_labirinto_tiff(self,img_array):
        
        """
        Parameters
        ----------
        img_array : array
              Prende in ingresso l'array tridimensionale restituito da leggi_file_tiff
              
              Legenda colori:
                  - [255 255 255]: pixel bianchi, sono posizioni che non assegnano punti, viene associato un costo pari a 1
                  - [0 0 0]: pixel neri, sono le pareti a cui viene associato valore NaN
                  - [0 255 0]: pixel verdi,indica la posizione di partenze del labirinto, viene associato un costo pari a 0
                  - [255 0 0]: Corrisponde al colore rosso, indica una posizione di destinazine del labirinto, viene associato un costo pari a 0. 
                  - [16 16 16], [32 32 32], [48 48 48], ..., [240 240 240]: sono valori di grigio, rappresentati da diverse tonalità di colore.
                     Ciascuno di essi viene assegnato a un costo specifico compreso tra 1.0 e 15.0.

        Returns
        -------
        None
        
        """
        legenda_colori={'[255 255 255]':1.,'[0 0 0]':np.nan,'[0 255 0]':0.,'[255 0 0]':0.,
                         '[16 16 16]':1.,'[32 32 32]':2.,'[48 48 48]':3.,'[64 64 64]':4.,'[80 80 80]':5.,
                         '[96 96 96]':6.,'[112 112 112]':7.,'[128 128 128]':8.,'[144 144 144]':9.,'[160 160 160]':10.,
                         '[176 176 176]':11.,'[192 192 192]':12.,'[208 208 208]':13.,'[224 224 224]':14.,'[240 240 240]':15.}
        