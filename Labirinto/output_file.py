# -*- coding: utf-8 -*-
"""
Created on Fri May 26 18:04:49 2023

"""
import numpy as np

class Output_file:
    """
    classe che implementa metodi di per la creazione dei file di output
    """
    def __init__(self, nome_labirinto):
        """
        Costruttore della classe Output_file
        
        parameters
        ----------
        nomefile= string
        
        Returns
        -------
        None.
        
        """
        self.percorso_cartella='./output'
        self.nome_labirinto=nome_labirinto
        self.percorso_file=self.percorso_cartella+'/'+self.nome_labirinto
        
    def crea_immagine_rgb(self,labirinto, partenze, destinazioni, cammini_minimi):
        """
        

        Parameters
        ----------
        labirinto : TYPE
            DESCRIPTION.
        partenze : TYPE
            DESCRIPTION.
        destinazioni : TYPE
            DESCRIPTION.
        cammini_minimi : TYPE
            DESCRIPTION.

        Returns
        -------
        immagine_rgb : TYPE
            DESCRIPTION.

        """
        altezza, larghezza = labirinto.shape
        #crea una matrice che per ogni posizione del labirinto che crea una tupla di tre zeri che sono i tre valori di RGB
        immagine_rgb = np.zeros((altezza, larghezza, 3), dtype=np.uint8)
        #in ogni posizione del labirinto con valore nan metto il colore nero (0,0,0) mentre il resto delle caselle le pongo bianche (255,255,255)
        for i in range(altezza):
            for j in range(larghezza):
                valore = labirinto[i, j]
                if np.isnan(valore):
                    immagine_rgb[i, j] = (0,0,0)
                else:
                    immagine_rgb[i, j] = (255,255,255)
        #in ogni coordinata specificata nel cammino metto il colore viola
        for i in range(len(cammini_minimi)):
            immagine_rgb[cammini_minimi[i][0]][cammini_minimi[i][1]]=(138, 43, 226)
        immagine_rgb[partenze[0]][partenze[1]]=(0,255,0)
        immagine_rgb[destinazioni[0][0]][destinazioni[0][1]]=(255,0,0)
        return immagine_rgb
        
