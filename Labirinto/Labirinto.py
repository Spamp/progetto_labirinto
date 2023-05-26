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
        
        """
        Costruttore della classe Labirinto

        Parameters
        ----------
        labirinto : array

        partenze : list
   
        destinazioni : list

        Returns
        -------
        None.

        """
        self.labirinto = labirinto
        self.partenze = partenze
        self.destinazioni = destinazioni
        self.righe, self.colonne = labirinto.shape
        self.grafo=()
        
        
    def crea_grafo(self):
        
        """
        Metodo che crea un grafo indiretto a partire dall'array labirinto

        Returns
        -------
        G : graph

        """
        #creo un'istanza del grafo
        G = nx.Graph()
        self.grafo=G
        
        # i tiene traccia della riga, row scorre il contenuto della riga
        for i, row in enumerate(self.labirinto): 
            # j tiene traccia della colonna, val contiene il valore della cella
            for j, val in enumerate(row):
            
                # se il valore della cella non è NaN (se la cella non è una parete) 
                if not np.isnan(val): 
                    
                #controlla se la cella corrente ha una cella adiacente sopra di essa, 
                #e se la cella adiacente non è una parete.
                
                    if i > 0 and not np.isnan(self.labirinto[i-1, j]):
                        # aggiungo l'arco di peso pari al valore della cella
                        G.add_edge((i, j), (i-1, j), weight= val) 
                        
                    if j > 0 and not np.isnan(self.labirinto[i, j-1]):
                        G.add_edge((i, j), (i,j-1), weight = val)
                   
                    if i < self.righe-1 and not np.isnan(self.labirinto[i+1, j]):
                        G.add_edge((i, j), (i+1, j), weight=val)
                        
                    if j < self.colonne-1 and not np.isnan(self.labirinto[i, j+1]):
                        G.add_edge((i, j), (i, j+1), weight= val)
        return self.grafo
    
    
    
    def cammino_minimo(self):
        
        """
        Metodo che trova il cammino minimo fra le partenze e le destinazioni, e restituisce il path
        del cammino e il peso ad esso associato

        Returns
        -------
        cammini_minimi : list
            Restituisce una lista di tuple contenente il path del cammino minimo
            
        weight_tot : list
            Restituisce una lista di liste contenenti il peso totale del cammino

        """
        
        # Trasformo ogni sottolista in una tupla
        partenze=[tuple(sublist) for sublist in self.partenze]
        partenze=tuple(partenze)
        destinazioni=[tuple(sublist) for sublist in self.destinazioni]
        destinazioni=tuple(destinazioni)
        
        # Converto le tuple in insiemi di nodi
        partenze_set = set(partenze)
        destinazioni_set = set(destinazioni)
        
        cammini_minimi = [] 
        weight_tot=[]
        
        # Scorro tutti i nodi di partenza e destinazione
        for nodo_p in partenze_set:
            for nodo_d in destinazioni_set:
                
                # verifico che i nodi di partenza e destinazione siano nel grafo
                if self.grafo.has_node(nodo_p) and self.grafo.has_node(nodo_d):
                    
                    # verifico che esista un path possibile fra nodo di partenza e destinazione 
                    if nx.has_path(self.grafo,nodo_p,nodo_d):
                        
                        # restituisce il path minimo pesato fra i nodi di partenza e destinazione
                        distance, cammino_minimo = nx.single_source_dijkstra(self.grafo, source=nodo_p, target=nodo_d, weight ='weight')
                        # aggiungo il cammino minimo trovato alla lista dei cammini minimi
                        cammini_minimi.append(cammino_minimo)
                        # aggiungo alla lista dei pesi il peso totale, dato dalla somma della lunghezza del cammino e dei pesi incontrati
                        weight_tot.append(distance+(len(cammino_minimo)-1))
                    else:
                        # se non esiste un path fra i nodi considerati, restituisce un messaggio di errore
                        raise ValueError("Non esiste un percorso possibile fra", nodo_p, "e", nodo_d)
                else:
                    # se i nodi considerati non appartengono al grafo, restituisce un messaggio di errore
                    raise ValueError("Il nodo", nodo_p, "oppure il nodo", nodo_d, "non sono presenti nel grafo")
                    
        return cammini_minimi, weight_tot
    
    

    
    
        
    
        

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

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
