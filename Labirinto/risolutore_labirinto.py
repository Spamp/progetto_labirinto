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
    Metodo che richiama i metodi implementati per risolvere il labirinto

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
    # calcolo tutti i cammini possibili fra partenza e destinazione, utilizzando un thread parallelo così
    #da evitare che il codice si blocchi    
    thread = threading.Thread(target=maze.trova_tutti_i_cammini)
    #avvio il thread
    thread.start()
    #blocco il codice principale per 10 secondi per dare il tempo al thread di fare tutte le sue operazioni
    time.sleep(5)

    #una volta svogliato il thread principale, controllo se il thread per cercare tutti i cammini è attivo
    if thread.is_alive():
        #se è ancora attivo provo a lasciralo lavorare ancora per 30 secondi
        thread.join(timeout=20)
        print("il thread ha trovato solo i cammini minimi, ma non altre soluzioni")
    else:
        #se il thread si è concluso lo chiudo
        thread.join()
        print('il thread si è concluso con successo: ha trovato tutti i cammini possibili')
    #richiedo l'attributo creato da tutti i cammini con un metodo, per evitare conflitti tra thread
    tutti_i_cammini_semplici=maze.get_attributo()      
    
    #creo un'istanza della classe Output_file
    outfile= Output_file(nome_labirinto)
    
    # restituisco i percorsi trovati
    outfile.crea_immagini_output(labirinto, partenze, destinazioni, shortest_path)

    tutti_i_cammini_minimi_dict={'tutti i cammini minimi':shortest_path,'costi':weight}
    outfile.crea_file_json(tutti_i_cammini_minimi_dict,'tutti i cammini minimi')
    outfile.crea_file_json(tutti_i_cammini_semplici,'tutti i cammini semplici')
    return (labirinto, partenze, destinazioni, shortest_path, weight, tutti_i_cammini_semplici)
