# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:47:28 2023

"""
import os
from input_file import Input_file
from labirinto import Labirinto
from output_file import Output_file
import threading
import time


def calcolatore():
    
    """
    Funzione che richiama i metodi implementati per risolvere il labirinto

    Returns
    -------
    labirinto: array 
    partenze: list
    destinazioni: list
    grafo: graph
    shortest_path: list of tuple
    weight: list

    """
    # ottieni i nomi dei file e delle cartelle nella directory
    lista_file = os.listdir('./indata/')
    print(lista_file)
    nomefile=str(input('Inserisci il nome del file da leggere con formato tiff o json tra uno di quelli elencati:  '))
    nomelist=nomefile.split('.')
    nome_labirinto=nomelist[0]
    #Chiedo il file di input e richiamo la funzione di lettura
    filepath = './indata/'+nomefile
    input_file=Input_file(filepath)
    (labirinto, partenze, destinazioni)=input_file.leggi_file()
    
    # creo un'istanza della classe Labirinto
    maze = Labirinto(labirinto, partenze, destinazioni)
    # calcolo il cammino minimo e il peso ad esso associato
    shortest_path, weight= maze.cammino_minimo()
    
    # Calcolo tutti i cammini possibili fra partenza e destinazione. Essendo un calcolo molto oneroso,
    # avviamo un thread per assegnare al metodo di ricerca di tutti i cammini semplici un tempo massimo di esecuzione.
    # Assegnamo un tempo massimo di 25 secondi totali, in seguito ai quali vengono restituiti tutti i cammini trovati.
    # Se il tempo di esecuzione del metodo supera il tempo massimo specificato, possiamo concludere
    # che il metodo ha trovato un numero troppo elevato di percorsi, che può essere potenzialmente infinito. 
    
    # richiamo un metodo che crea un thread che scorre la funzione trova_tutti_i_cammini   
    thread = threading.Thread(target=maze.trova_tutti_i_cammini)
    #avvio il thread appena creato
    thread.start()
    #blocco il codice principale per 5 secondi per dare il tempo al thread di calcolare tutti i cammini
    time.sleep(5)
    # quando termina il blocco, controllo se il thread per cercare tutti i cammini è attivo (non è ancora termato)
    if thread.is_alive():
        #se è ancora attivo, gli lascio altri 20 secondi per trovare tutti i cammini
        thread.join(timeout=20)
        # se dopo 20 secondi (25 totali) non si è ancora concluso, potrei avere cammini infiniti
        print("il thread ha trovato solo i cammini minimi, ma non altre soluzioni")
    else:
        #se il thread non è più attivo (quindi si è concluso trovando tutti i cammini), si chiude
        thread.join()
        # se il thread si è chiuso, restituisce un messaggio 
        print('il thread si è concluso con successo: ha trovato tutti i cammini possibili')
        
    # richiamo il metodo che mi restituisce gli attributi della classe labirinto "cammini_semplici" e 
    # "pesi_cammini_semplici". 
    cammini_semplici,pesi_cammini_semplici=maze.get_attributo()      
    
    #creo un'istanza della classe Output_file
    outfile= Output_file(nome_labirinto)
    
    # restituisco i percorsi trovati
    outfile.crea_immagini_output(labirinto, partenze, destinazioni, shortest_path)

    outfile.crea_file_json(shortest_path,weight,'tutti i cammini minimi')
    outfile.crea_file_json(cammini_semplici,pesi_cammini_semplici,'tutti i cammini semplici')
    return (labirinto, partenze, destinazioni, shortest_path, weight)
