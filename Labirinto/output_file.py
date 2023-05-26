# -*- coding: utf-8 -*-
"""
Created on Fri May 26 18:04:49 2023

"""
import numpy as np
from PIL import Image

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
        
    def crea_immagini_output(self,labirinto, partenze,destinazioni, shortest_path):
        #scorro le partenze per avere un matrice rgb per ogni partenza e percorso associato
        for i in range(len(partenze)):
            immagine_rgb = Output_file.crea_immagine_rgb(self,labirinto, partenze[i],destinazioni, shortest_path[i])
            Output_file.salva_immagine_jpg(self,immagine_rgb, i)
        
    def crea_immagine_rgb(self,labirinto, partenze, destinazioni, cammini_minimi):
        """
        metodo che a partire dalle liste descrttive del labirinto crea un lista che per ogni casella del
        labirinto pone una tupla di tre componenti che corrispondono ai valori rgb del pixel corrispondente.
        

        Parameters
        ----------
        labirinto : array

        partenze : list of lists
   
        destinazioni : list of lists
        
        cammini_minimi : list of tuples

        Returns
        -------
        immagine_rgb : list

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
    
    def salva_immagine_jpg(self, immagine_rgb,numero_immagine):
        #creo percorso dove salvare l'immagine
        percorso_immagine= self.percorso_file+f'_{numero_immagine}.jpeg'
        dimensioni= immagine_rgb.shape
        altezza=dimensioni[0]
        larghezza =dimensioni[1]
        #creazione dell'immagine dal lista di valori rgb
        immagine = Image.fromarray(immagine_rgb)
        #imposta la grandezza dell'immagine jpg di modo che sia la stessa del labirinto
        area_visualizzazione=(0,0,larghezza,altezza)
        immagine_cropped = immagine.crop(area_visualizzazione)
        #salva l'immagine nel percorso specificato
        immagine_cropped.save(percorso_immagine, "JPEG")
        
