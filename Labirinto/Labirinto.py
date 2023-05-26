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
    
    