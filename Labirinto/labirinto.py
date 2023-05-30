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
        self.cammini={}
        
        
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
        # richiamo direttamento il metodo che crea il grafo
        self.crea_grafo()
        
        # Trasformo le liste di partenza e destinazione in tuple, poichè immutabili, quindi più sicure e prestanti
        partenze=tuple([tuple(sublist) for sublist in self.partenze])
        destinazioni=tuple([tuple(sublist) for sublist in self.destinazioni])
               
        # Converto le tuple contenenti i nodi di partenza e destinazione in un insieme set, per facilitare la verifica
        # della presenza dei nodi considerati nel grafo di partenza, sfruttando la proprietà di unicità degli elementi
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
                        #inserico un cammino vuoto all'interno della lista dei cammini se non esiste un percorso tra i nodi specificati
                        cammini_minimi.append(())
                        #inserisco un messaggio che non esiste un percorso e quindi neanche un peso nella lista di pesi, mettendolo nell'indice corrispondente al cammino vuoto 
                        weight_tot.append((f"Non esiste un percorso possibile fra {nodo_p} e {nodo_d}"))
                else:
                    # se i nodi considerati non appartengono al grafo, restituisce un messaggio di errore
                    raise ValueError("Il nodo", nodo_p, "oppure il nodo", nodo_d, "non sono presenti nel grafo")
                    
        return cammini_minimi, weight_tot
    
    def trova_tutti_i_cammini(self):
        """
        metodo che dal grafo creato in precendenza, cerca tutti i cammini possibili tra le partenze e
        destinazioni. Ritorna un dizionario con una lista di tuple di tutti i cammini possibili ed una 
        lista di tutti i costi associati per indice delle liste.

        Returns
        -------
        dizionario.

        """
        
        # Trasforma ogni sottolista in una tupla
        partenze=tuple([tuple(sublist) for sublist in self.partenze])
        destinazioni=tuple([tuple(sublist) for sublist in self.destinazioni])
        
        #Calcolo tutti i possibili cammini fra partenza/e e destinazione/i
        cammini = []
        len_cammini=[]
        peso_archi=[]
        weight_tot=[]
        
        for partenza in partenze:
            for destinazione in destinazioni:
                
                # verifico che i nodi di partenza e destinazione siano nel grafo
                if self.grafo.has_node(partenza) and self.grafo.has_node(destinazione):
                    
                    # verifico che esista un path possibile fra nodo di partenza e destinazione
                    if nx.has_path(self.grafo, partenza, destinazione):
                        # calcolo tutti i cammini possibili fra il nodo di partenza e quello di destinazione (cutoff=None, è la profondità massima di esplorazione)
                        for cammino in list(nx.all_simple_paths(self.grafo, source=partenza, target=destinazione, cutoff=None)):
                            # aggiungo il cammino trovato alla lista dei cammini
                            cammini.append(cammino)
                            # aggiungo la lunghezza del cammino alla lista len_cammini
                            len_cammini.append(len(cammino)-1)
                            # per ogni cammino trovato, calcolo il peso del path
                            peso_archi_cammino = sum(self.grafo[u][v]['weight'] for u, v in zip(cammino[:-1], cammino[1:]))
                            # aggiunto i pesi trovati alla lista peso_archi
                            peso_archi.append(peso_archi_cammino)
        
        # calcolo il costo totale del cammino, dato dalla somma dei pesi e della lunghezza del cammino
        weight_tot=[x+y for x,y in zip(len_cammini, peso_archi)]
                            
        #creo un dizionario con i risultati di tutti i cammini con i costi associati per indice
        dizionario={'tutti i cammini possibili':cammini,'costo':weight_tot}
        self.cammini=dizionario
        return  self.cammini
    
    def get_attributo(self):
        """
        metodo che ritorna l'attributo della classe cammini, creato in precendenza dal metodo
        trova_tutti_i_cammini

        Returns
        -------
        TYPE
            dizionario

        """
        return self.cammini
    
    
    

        
    
