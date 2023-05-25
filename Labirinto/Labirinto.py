# -*- coding: utf-8 -*-
"""
Created on Tue May 23 13:51:57 2023

"""
import numpy as np
import networkx as nx


class Labirinto:
    """
    Classe che implementa il labirinto
    
    """
        
    def __init__(self, labirinto, partenze, destinazioni):
        self.labirinto = labirinto
        self.partenze = partenze
        self.destinazioni = destinazioni
        self.righe, self.colonne = labirinto.shape
        
        
    def crea_grafo(self):
        """
        Metodo che crea un grafo a partire dal labirinto

        Returns
        -------
        G : graph

        """
        #creo un'istanza del grafo
        G = nx.Graph()
        for i, row in enumerate(self.labirinto): #i tiene traccia della riga, row contiene la riga
            for j, val in enumerate(row): #j tiene conto della colonna, val del valore della cella
                # se l'elemento della cella non è nan 
                if not np.isnan(val): 
                #controlla se la cella corrente ha una cella adiacente sopra di essa, 
                #e se la cella adiacente non è una parete.
                    if i > 0 and not np.isnan(self.labirinto[i-1, j]):
                        # aggiungo l'arco di peso pari al valore della cella
                        G.add_edge((i, j), (i-1, j), weight= val) 
                    if j > 0 and not np.isnan(self.labirinto[i, j-1]):
                        G.add_edge((i, j), (i,j-1), weight = val)
                    # Costruisco un grafo indiretto
                    if i < self.righe-1 and not np.isnan(self.labirinto[i+1, j]):
                        G.add_edge((i, j), (i+1, j), weight=val)
                    if j < self.colonne-1 and not np.isnan(self.labirinto[i, j+1]):
                        G.add_edge((i, j), (i, j+1), weight= val)
        return G
    
    
    
    def cammino_minimo(self, grafo):
        
        # Trasforma ogni sottolista in una tupla
        partenze=[tuple(sublist) for sublist in self.partenze]
        partenze=tuple(partenze)
        destinazioni=[tuple(sublist) for sublist in self.destinazioni]
        destinazioni=tuple(destinazioni)
        
        # converti in insiemi di nodi
        partenze_set = set(partenze)
        destinazioni_set = set(destinazioni)
        cammini_minimi = [] #calcola i cammini minimi fra partenza/e e destinazione/i
        lunghezza_cammino=[]
        
        # scorri tutte le coppie di partenza e destinazione
        for nodo_p in partenze_set:
            for nodo_d in destinazioni_set:
                # verifico che i nodi di partenza e destinazione siano nel grafo
                if grafo.has_node(nodo_p) and grafo.has_node(nodo_d):
                    # verifico che esista un path possibile fra nodo di partenza e destinazione 
                    if nx.has_path(grafo,nodo_p,nodo_d):
                        #Returns the shortest weighted path from source to target in G.
                        distance, cammino_minimo = nx.single_source_dijkstra(grafo, source=nodo_p, target=nodo_d, weight ='weight')
                        cammini_minimi.append(cammino_minimo)
                        lunghezza_cammino.append(distance+(len(cammino_minimo)-1))
                        
        return cammini_minimi, lunghezza_cammino
    
    

    
    
        
    
        

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

# =============================================================================
#     def crea_labirinto_json(self,dict):
#         """
#         
#         Metodo che crea il labirinto a partire dal dizionario generato dalla lettura 
#         del file con estensione .json
#         
#         Parameters
#         ----------
#         dict: dict
#             prende in ingresso il dizionario con le caratteristiche del labirinto
# 
#         Returns
#         -------
#         Labirinto: array 
#         Partenze: list
#         Destinazioni: list
# 
#         """
#         #creo una matrice numpy di soli 1, con altezza e larghezza specificate nel dizionario
#         maze= np.full((dict['altezza'], dict['larghezza']), 1.)
#         # creo la lista con le partenze specificate nel dizionario
#         partenze=dict['iniziali']
#         # creo la lista con le destinazioni specificate nel dizionario
#         destinazioni=dict['finale']
#         
#         # creo le pareti sostiuendo gli 1 con il valore NaN
#         for i in range(len(dict['pareti'])):
#             if dict['pareti'][i]['orientamento']=='H':
#                 indice1=int(dict['pareti'][i]['posizione'][0])
#                 indice2=int(dict['pareti'][i]['posizione'][1])
#                 indice3=int(dict['pareti'][i]['posizione'][1])+int(dict['pareti'][i]['lunghezza'])
#                 maze[indice1,indice2:indice3]=np.nan
#             else:
#                 indice1=int(dict['pareti'][i]['posizione'][0])
#                 indice2=int(dict['pareti'][i]['posizione'][0])+int(dict['pareti'][i]['lunghezza'])
#                 indice3=int(dict['pareti'][i]['posizione'][1])
#                 maze[indice1:indice2,indice3]=np.nan
#                 
#         # sostuisco le posizioni specificate nel dizioanrio con il costo 
#         for i in range(len(dict['costi'])):
#             posizione_orizzontale=dict['costi'][i][0]
#             posizione_verticale=dict['costi'][i][1]
#             maze[posizione_orizzontale,posizione_verticale]=float(dict['costi'][i][2])
#         return (maze, partenze, destinazioni)
#     
#     
#     def crea_labirinto_tiff(self,img_array):
#         
#         """
#         Metodo che crea il labirinto a partire dall'array generato dalla lettura 
#         del file con estensione .tiff
#         
#         Parameters
#         ----------
#         img_array : array
#               Prende in ingresso l'array tridimensionale restituito da leggi_file_tiff
#               
#               Legenda colori:
#                   - [255 255 255]: pixel bianchi, sono posizioni che non assegnano punti, costo pari a 1
#                   - [0 0 0]: pixel neri, sono le pareti a cui viene associato valore NaN
#                   - [0 255 0]: pixel verdi,indica la posizione di partenze del labirinto, costo pari a 0
#                   - [255 0 0]: Corrisponde al colore rosso, indica una posizione di destinazine del labirinto, costo pari a 0. 
#                   - [16 16 16], [32 32 32], [48 48 48], ..., [240 240 240]: sono valori di grigio, rappresentati da diverse 
#                   tonalità di colore.Ciascuno di essi viene assegnato a un costo specifico compreso tra 1.0 e 15.0.
# 
#         Returns
#         -------
#         Labirinto: array
#         Partenze: list
#         Destinazioni: list
#         
#         """
#         legenda_colori={'[255 255 255]':1.,'[0 0 0]':np.nan,'[0 255 0]':0.,'[255 0 0]':0.,
#                          '[16 16 16]':1.,'[32 32 32]':2.,'[48 48 48]':3.,'[64 64 64]':4.,'[80 80 80]':5.,
#                          '[96 96 96]':6.,'[112 112 112]':7.,'[128 128 128]':8.,'[144 144 144]':9.,'[160 160 160]':10.,
#                          '[176 176 176]':11.,'[192 192 192]':12.,'[208 208 208]':13.,'[224 224 224]':14.,'[240 240 240]':15.}
#         
#         
#         # ottengo le dimensioni del labirinto
#         forma_lab = img_array.shape
#         # creo il labirinto utilizzando le dimensioni dell'array
#         maze = np.full((forma_lab[0],forma_lab[1]),np.empty)
#         
#         partenze=[]
#         destinazioni=[]
#         for i in range(forma_lab[0]):
#             for j in range(forma_lab[1]):
#                 
#                 indice = f'[{img_array[i][j][0]} {img_array[i][j][1]} {img_array[i][j][2]}]'
#                 maze[i,j] = legenda_colori[indice]
#                 
#                 # Se il pixel è rosso, indica una posizione di destinazione del labirinto: 
#                     #inserisco la coordinata nella lista destinazioni
#                 if indice =='[255 0 0]':
#                     coordinate=[]
#                     coordinate.append(i)
#                     coordinate.append(j)
#                     destinazioni.append(coordinate)
#                     
#                 # Se il pixel è verde, indica una posizione di partenza del labirinto: 
#                     #inserisco la coordinata nella lista partenze
#                 elif indice =='[0 255 0]':
#                     coordinate=[]
#                     coordinate.append(i)
#                     coordinate.append(j)
#                     partenze.append(coordinate)
#         
#         return (maze, partenze, destinazioni)
#         
#         
# =============================================================================
