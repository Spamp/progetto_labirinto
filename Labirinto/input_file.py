# -*- coding: utf-8 -*-
"""
Created on Tue May 23 13:41:20 2023

"""
import os
import json
import numpy as np

from PIL import Image


class Input_file:
    
    """
    Classe che implementa e gestisce l'input
    
    Il programma riceve in ingresso:
        - il file, in formato .json o .tiff
        - il/i punto/i di partenza e arrivo
        
    """
    
    def __init__(self, filepath):
        
        """
        Costruttore della classe Input_file
    
        Parameters
        ----------
        filepath : str
            Contiene il path del file da leggere

        Returns
        -------
        None.

        """
        
        self.filepath = filepath
        
        
    def crea_labirinto_json(dict):
        
        """
        
        Metodo che crea il labirinto a partire dal file con estensione .json
        
        Parameters
        ----------
        dict: dict
            prende in ingresso un dizionario con le caratteristiche del labirinto

        Returns
        -------
        maze: array
            Restituisce il labirinto sotto forma di array di float
        
        partenze: list
            Restituisce la lista dei punti di partenza del labirinto
            
        destinazioni: list
            Restituisce la lista dei punti di destinazione del labirinto

        """
        #creo una matrice numpy di soli 1, con altezza e larghezza specificate nel dizionario
        maze= np.full((dict['altezza'], dict['larghezza']), 0.)
        # creo la lista con le partenze specificate nel dizionario
        partenze=dict['iniziali']
        # creo la lista con le destinazioni specificate nel dizionario
        destinazioni=dict['finale']
        
        # creo le pareti sostiuendo gli 1 con il valore NaN
        for i in range(len(dict['pareti'])):
            #distingue se la parete è orizzontale grazie al paramtro H
            if dict['pareti'][i]['orientamento']=='H':
                indice1=int(dict['pareti'][i]['posizione'][0])
                indice2=int(dict['pareti'][i]['posizione'][1])
                indice3=int(dict['pareti'][i]['posizione'][1])+int(dict['pareti'][i]['lunghezza'])
                maze[indice1,indice2:indice3]=np.nan
            #altrimentiè verticale, grazie al parametro V
            else:
                indice1=int(dict['pareti'][i]['posizione'][0])
                indice2=int(dict['pareti'][i]['posizione'][0])+int(dict['pareti'][i]['lunghezza'])
                indice3=int(dict['pareti'][i]['posizione'][1])
                maze[indice1:indice2,indice3]=np.nan
                
        # sostuisco le posizioni specificate nel dizioanrio con il costo specificato nella terza posizione 
        for i in range(len(dict['costi'])):
            posizione_orizzontale=dict['costi'][i][0]
            posizione_verticale=dict['costi'][i][1]
            maze[posizione_orizzontale,posizione_verticale]=float(dict['costi'][i][2])
        return (maze, partenze, destinazioni)
    
    def crea_labirinto_tiff(img_array):
        
        """
        Metodo che crea il labirinto a partire dal file con estensione .tiff
        
        Parameters
        ----------
        img_array : array
              Prende in ingresso un array tridimensionale con le caratteristiche del labirinto
              
              Legenda colori:
                  - [255 255 255]: pixel bianchi, sono posizioni che non assegnano punti, costo pari a 1
                  - [0 0 0]: pixel neri, sono le pareti a cui viene associato valore NaN
                  - [0 255 0]: pixel verdi,indica la posizione di partenze del labirinto, costo pari a 0
                  - [255 0 0]: Corrisponde al colore rosso, indica una posizione di destinazine del labirinto, costo pari a 0. 
                  - [16 16 16], [32 32 32], [48 48 48], ..., [240 240 240]: sono valori di grigio, rappresentati da diverse 
                  tonalità di colore.Ciascuno di essi viene assegnato a un costo specifico compreso tra 1.0 e 15.0.

        Returns
        -------
        maze: array
            Restituisce il labirinto sotto forma di array di float
            
        partenze: list
            Restituisce la lista dei punti di partenza del labirinto
            
        destinazioni: list
            Restituisce la lista dei punti di destinazione del labirinto
        
        """
        
        legenda_colori={'[255 255 255]':0.,'[0 0 0]':np.nan,'[0 255 0]':0.,'[255 0 0]':0.,
                         '[16 16 16]':1.,'[32 32 32]':2.,'[48 48 48]':3.,'[64 64 64]':4.,'[80 80 80]':5.,
                         '[96 96 96]':6.,'[112 112 112]':7.,'[128 128 128]':8.,'[144 144 144]':9.,'[160 160 160]':10.,
                         '[176 176 176]':11.,'[192 192 192]':12.,'[208 208 208]':13.,'[224 224 224]':14.,'[240 240 240]':15.}
        
        
        # ottengo le dimensioni del labirinto
        forma_lab = img_array.shape
        
        # creo il labirinto utilizzando le dimensioni dell'array
        maze = np.full((forma_lab[0],forma_lab[1]),np.empty)
        
        partenze=[]
        destinazioni=[]
        for i in range(forma_lab[0]):
            for j in range(forma_lab[1]):
                
                indice = f'[{img_array[i][j][0]} {img_array[i][j][1]} {img_array[i][j][2]}]'
                maze[i,j] = legenda_colori[indice]
                
                # Se il pixel è rosso, indica una posizione di destinazione del labirinto: 
                    #inserisco la coordinata nella lista destinazioni
                if indice =='[255 0 0]':
                    coordinate=[]
                    coordinate.append(i)
                    coordinate.append(j)
                    destinazioni.append(coordinate)
                    
                # Se il pixel è verde, indica una posizione di partenza del labirinto: 
                    #inserisco la coordinata nella lista partenze
                elif indice =='[0 255 0]':
                    coordinate=[]
                    coordinate.append(i)
                    coordinate.append(j)
                    partenze.append(coordinate)
        
        return (maze, partenze, destinazioni)
    
    
    def leggi_file(self):
       
        """
        Metodo che restituisce il labirinto sotto forma di dizionario o array, in base
        al formato del file di input (.json o .tiff)

        Parameters
        ----------
        filepath : str
            prende in ingresso il path del file da leggere in formato json

        Returns
        -------
        (labirinto, partenze, destinazioni): matrice numpy con i pesi del labirinto, lista di liste delle coordinate
                                            di partenza e lista di liste con le coordinate di destinazione
            
        """
        #splitto la stringa filepath per isolare il nome del file e il formato
        percorso,estensioneFile = os.path.splitext(self.filepath)
        percorsolist=percorso.split('/')
        nome=percorsolist[2]
        nomefile=nome+estensioneFile
        lista_file = os.listdir('./indata/')
        
        #controlla che il nome del file sia all'interno della cartella 
        if nomefile in lista_file:
            if estensioneFile == '.json':
                dictionary=Input_file.leggi_file_json(self)
                
                #richiamo diretto il metodo per creare il labirinto da file json
                (labirinto, partenze, destinazioni)=Input_file.crea_labirinto_json(dictionary)
                return (labirinto, partenze, destinazioni)
            elif estensioneFile == '.tiff':
                img_array =Input_file.leggi_file_tiff(self)
                #richiamo diretto il metodo per creare il labirinto da file tiff
                (labirinto, partenze, destinazioni)=Input_file.crea_labirinto_tiff(img_array)
                return (labirinto, partenze, destinazioni)
        #se il file non si trova all'interno della cartella indata, richiedo di nuovo l'input e richiamo il metodo
        else:
            lista_file = os.listdir('./indata/')
            print(lista_file)
            filepath='./indata/'+str(input('il file cercato non è presente nella cartella. Prova con un altro nome: '))
            return Input_file.leggi_file(filepath)

        
        
    def leggi_file_json(self):
       
        """
        Metodo che restituisce il dizionario contenente le caratteristiche del labirinto

        Parameters
        ----------
        filepath : str
            prende in ingresso il path del file da leggere in formato json

        Returns
        -------
        dictionary : dict
            Restituisce un dizionario con le caratteristiche del labirinto
        
        """
        
        with open(self.filepath) as file:
            dictionary = json.load(file)
        return dictionary 
    
    
    def leggi_file_tiff(self):
        
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
            Restituisce un array con le caratteristiche del labirinto
        
        """
     
        with Image.open(self.filepath) as img:
            # Converte l'immagine in una matrice NumPy
            img_array = np.array(img)
            return img_array
        
       