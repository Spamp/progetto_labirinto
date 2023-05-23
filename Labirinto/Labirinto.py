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